import os
from datetime import datetime, timezone
from pyexpat import model
from typing import Dict, List, Literal, cast
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field, SecretStr
from src.react_agent.prompts import MANAGER_PROMPT, STATUS_PROMPT
from src.react_agent.configuration import Configuration
from src.react_agent.state import AgentState, InputState, State
from src.react_agent.tools import MANAGER_TOOLS, MONITOR_TOOLS
from src.react_agent.utils import load_chat_model, load_openai_chat_model
from langgraph.checkpoint.memory import MemorySaver
import dotenv
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

dotenv.load_dotenv()
memory = MemorySaver()
llm = load_openai_chat_model()
members = [
    {
        "name": "status_agent",
        "introduction": "status_agent can provide status of short links",
    },
    {
        "name": "manager_agent",
        "introduction": "manager_agent can create, delete or update short links",
    },
    {
        "name": "support_agent",
        "introduction": "support_agent can provide support for short links customers, call this agent if you need to contact human"
    },
]

member_names = [member["name"] for member in members]
options = member_names + ["FINISH"]
config = Configuration.from_runnable_config()


class Router(TypedDict):
    """Worker to route to next. If no workers needed, route to FINISH."""

    next: Literal[*options]


async def supervisor_node(state: AgentState):
    messages = [
        {
            "role": "system",
            "name": "supervisor",
            "content": "You are a supervisor tasked with managing a conversation between the"
            f" following workers: {members}. Given the following user request,"
            " respond with the worker to act next. Each worker will perform a"
            " task and respond with their results and status. When finished or need human intervention, respond with FINISH.",
        },
    ] + state["messages"]
    response = await llm.with_structured_output(Router).ainvoke(messages)
    next_ = response["next"]
    if next_ == "FINISH":
        next_ = END

    return {"next": next_}


status_agent = create_react_agent(
    model=llm,
    tools=MONITOR_TOOLS,
    state_modifier=STATUS_PROMPT.format(
        system_time=datetime.now(tz=timezone.utc).isoformat()
    ),
)


async def status_node(state: AgentState):
    response = await status_agent.ainvoke(state)

    return {
        "messages": [
            HumanMessage(content=response["messages"][-1].content, name="status_agent")
        ]
    }


manager_agent = create_react_agent(
    model=llm,
    tools=MANAGER_TOOLS,
    state_modifier=MANAGER_PROMPT.format(
        system_time=datetime.now(tz=timezone.utc).isoformat()
    ),
)


async def manager_node(state: AgentState):
    response = await manager_agent.ainvoke(state)

    return {
        "messages": [
            HumanMessage(content=response["messages"][-1].content, name="manager_agent")
        ]
    }

support_agent = create_react_agent(
    model=llm,
    tools=SUPPORT_TOOLS,
    state_modifier=SUPPORT_PROMPT.format(
        system_time=datetime.now(tz=timezone.utc).isoformat()
    ),
)

async def support_node(state: AgentState):
    response = await support_agent.ainvoke(state)

    return {
        "messages": [
            HumanMessage(content=response["messages"][-1].content, name="support_agent")
        ]
    }

# Define a new graph

# builder = StateGraph(State, input=InputState, config_schema=Configuration)

builder = StateGraph(AgentState)
builder.add_edge(START, "supervisor")
builder.add_node("supervisor", supervisor_node)
builder.add_node("status_agent", status_node)
builder.add_node("manager_agent", manager_node)
builder.add_node("support_agent", support_node)


for member in member_names:
    # We want our workers to ALWAYS "report back" to the supervisor when done
    builder.add_edge(member, "supervisor")

    # The supervisor populates the "next" field in the graph state
# which routes to a node or finishes
builder.add_conditional_edges("supervisor", lambda state: state["next"])

# Compile the builder into an executable graph
# You can customize this by adding interrupt points for state updates
graph = builder.compile(
    interrupt_before=[],  # Add node names here to update state before they're called
    interrupt_after=[],  # Add node names here to update state after they're called
    checkpointer=memory,
)
graph.name = "ReAct Agent"  # This customizes the name in LangSmith
