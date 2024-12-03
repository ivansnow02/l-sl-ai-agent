"""Utility & helper functions."""

import os
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from pydantic import SecretStr


def get_message_text(msg: BaseMessage) -> str:
    """Get the text content of a message."""
    content = msg.content
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return content.get("text", "")
    else:
        txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
        return "".join(txts).strip()


def load_chat_model(fully_specified_name: str) -> BaseChatModel:
    """Load a chat model from a fully specified name.

    Args:
        fully_specified_name (str): String in the format 'provider/model'.
    """
    provider, model = fully_specified_name.split("/", maxsplit=1)
    return init_chat_model(model, model_provider=provider)


def load_openai_chat_model(
    token=os.environ["GITHUB_TOKEN"],
    endpoint=os.environ["OPENAI_API_BASE"],
    model_name=os.environ["MODEL_NAME"],
) -> ChatOpenAI:
    return ChatOpenAI(
        model=model_name, api_key=SecretStr(token), base_url=endpoint, temperature=1
    )
