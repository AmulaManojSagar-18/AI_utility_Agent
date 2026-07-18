"""Session memory helpers for the LangChain agent.

The old implementation had no conversation memory. LangChain's in-memory
checkpointer keeps chat history available for the current terminal session while
avoiding deprecated memory classes.
"""

from __future__ import annotations

from uuid import uuid4

from langgraph.checkpoint.memory import InMemorySaver


SESSION_ID = uuid4().hex
CHECKPOINTER = InMemorySaver()


def get_session_config(session_id: str | None = None) -> dict[str, dict[str, str]]:
    """Build the runnable config that keeps one chat thread per CLI session."""

    return {"configurable": {"thread_id": session_id or SESSION_ID}}


def get_checkpointer() -> InMemorySaver:
    """Return the shared in-memory checkpointer used by the agent."""

    return CHECKPOINTER