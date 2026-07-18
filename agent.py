"""LangChain agent wiring for the AI Utility Agent.

The old manual `if`/`elif` router is replaced by LangChain's agent graph, which
chooses tools and executes them automatically.
"""

from __future__ import annotations

from collections.abc import Iterable

from langchain.agents import create_agent
from langchain_core.messages import AIMessage

from gemini_client import get_chat_model
from memory import get_checkpointer, get_session_config
from prompts import build_system_prompt
from tools import calculator, send_email, summarize, weather


TOOLS = [calculator, weather, send_email, summarize]
AGENT = create_agent(
    model=get_chat_model(),
    tools=TOOLS,
    system_prompt=build_system_prompt(),
    checkpointer=get_checkpointer(),
)


def _extract_final_answer(messages: Iterable[object]) -> str:
    """Return the last AI message content as a plain string."""

    for message in reversed(list(messages)):
        if isinstance(message, AIMessage):
            content = message.content
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                parts: list[str] = []
                for item in content:
                    if isinstance(item, dict):
                        parts.append(str(item.get("text", "")))
                    else:
                        parts.append(str(item))
                return "".join(parts).strip()
            return str(content)
    return ""


def run_agent(user_input: str, session_id: str | None = None) -> str:
    """Run the LangChain agent for one user message.

    The same session ID keeps the current conversation history alive in memory.
    """

    try:
        result = AGENT.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=get_session_config(session_id),
        )
        return _extract_final_answer(result.get("messages", [])) or "No response generated."
    except Exception as exc:
        return f"Agent error: {exc}"