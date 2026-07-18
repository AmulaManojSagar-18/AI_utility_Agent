"""LangChain tools used by the AI Utility Agent.

Each function keeps the same behavior as the pre-LangChain project, but the
`@tool` decorator turns it into a first-class LangChain tool with a name,
description, and callable implementation.
"""

from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """Evaluate a simple math expression and return the result as text."""

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Invalid Expression"


@tool
def weather(city: str) -> str:
    """Return a mock weather update for a city."""

    if not city.strip():
        return "Please provide a city name for the weather lookup."

    return f"It is currently sunny in {city} with 31°C."


@tool
def send_email(receiver: str, message: str) -> str:
    """Return a mock email confirmation for the given receiver and message."""

    if not receiver.strip() or not message.strip():
        return "Please provide both a receiver and a message for the email tool."

    return f"Email sent to {receiver} with message: {message}"


@tool
def summarize(text: str) -> str:
    """Summarize long text by keeping the first 20 words."""

    if not text.strip():
        return "Please provide text to summarize."

    words = text.split()

    if len(words) <= 20:
        return text

    return " ".join(words[:20]) + "..."