"""Define a custom Reasoning and Action agent.

Works with a chat model with tool calling support.
"""

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
from src.react_agent.prompts import SYSTEM_PROMPT
from src.react_agent.configuration import Configuration
from src.react_agent.state import AgentState, InputState, State
from src.react_agent.tools import MONITOR_TOOLS
from src.react_agent.utils import load_chat_model, load_openai_chat_model
from langgraph.checkpoint.memory import MemorySaver
import dotenv
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

dotenv.load_dotenv()
memory = MemorySaver()
# Define the function that calls the model


# async def call_model(
#     state: State, config: RunnableConfig
# ) -> Dict[str, List[AIMessage]]:
#     """Call the LLM powering our "agent".

#     This function prepares the prompt, initializes the model, and processes the response.

#     Args:
#         state (State): The current state of the conversation.
#         config (RunnableConfig): Configuration for the model run.

#     Returns:
#         dict: A dictionary containing the model's response message.
#     """
#     configuration = Configuration.from_runnable_config(config)

#     # Initialize the model with tool binding. Change the model or add more tools here.
#     model = load_openai_chat_model().bind_tools(MONITOR_TOOLS)

#     # Format the system prompt. Customize this to change the agent's behavior.
#     system_message = configuration.system_prompt.format(
#         system_time=datetime.now(tz=timezone.utc).isoformat()
#     )

#     # Get the model's response
#     response = cast(
#         AIMessage,
#         await model.ainvoke(
#             [{"role": "system", "content": system_message}, *state.messages], config
#         ),
#     )

#     # Handle the case when it's the last step and the model still wants to use a tool
#     if state.is_last_step and response.tool_calls:
#         return {
#             "messages": [
#                 AIMessage(
#                     id=response.id,
#                     content="Sorry, I could not find an answer to your question in the specified number of steps.",
#                 )
#             ]
#         }

#     # Return the model's response as a list to be added to existing messages
#     return {"messages": [response]}
llm = load_openai_chat_model()
members = ["status_agent"]
options = members + ["FINISH"]


class Router(TypedDict):
    """Worker to route to next. If no workers needed, route to FINISH."""

    next: Literal[*options]


async def supervisor_node(state: AgentState) -> AgentState:
    messages = [
        {
            "role": "system",
            "name": "supervisor",
            "content": "You are a supervisor tasked with managing a conversation between the"
            f" following workers: {members}. Given the following user request,"
            " respond with the worker to act next. Each worker will perform a"
            " task and respond with their results and status. When finished,"
            " respond with FINISH.",
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
    state_modifier=SYSTEM_PROMPT.format(
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


# Define a new graph

# builder = StateGraph(State, input=InputState, config_schema=Configuration)

builder = StateGraph(AgentState)
builder.add_edge(START, "supervisor")
builder.add_node("supervisor", supervisor_node)
builder.add_node("status_agent", status_node)


for member in members:
    # We want our workers to ALWAYS "report back" to the supervisor when done
    builder.add_edge(member, "supervisor")

    # The supervisor populates the "next" field in the graph state
# which routes to a node or finishes
builder.add_conditional_edges("supervisor", lambda state: state["next"])

# # Define the two nodes we will cycle between
# builder.add_node(call_model)
# builder.add_node("tools", ToolNode(tools=MONITOR_TOOLS))

# # Set the entrypoint as `call_model`
# # This means that this node is the first one called
# builder.add_edge("__start__", "call_model")


# def route_model_output(state: State) -> Literal["__end__", "tools"]:
#     """Determine the next node based on the model's output.

#     This function checks if the model's last message contains tool calls.

#     Args:
#         state (State): The current state of the conversation.

#     Returns:
#         str: The name of the next node to call ("__end__" or "tools").
#     """
#     last_message = state.messages[-1]
#     if not isinstance(last_message, AIMessage):
#         raise ValueError(
#             f"Expected AIMessage in output edges, but got {type(last_message).__name__}"
#         )
#     # If there is no tool call, then we finish
#     if not last_message.tool_calls:
#         return "__end__"
#     # Otherwise we execute the requested actions
#     return "tools"


# # Add a conditional edge to determine the next step after `call_model`
# builder.add_conditional_edges(
#     "call_model",
#     # After call_model finishes running, the next node(s) are scheduled
#     # based on the output from route_model_output
#     route_model_output,
# )

# # Add a normal edge from `tools` to `call_model`
# # This creates a cycle: after using tools, we always return to the model
# builder.add_edge("tools", "call_model")

# Compile the builder into an executable graph
# You can customize this by adding interrupt points for state updates
graph = builder.compile(
    interrupt_before=[],  # Add node names here to update state before they're called
    interrupt_after=[],  # Add node names here to update state after they're called
    checkpointer=memory,
)
graph.name = "ReAct Agent"  # This customizes the name in LangSmith
