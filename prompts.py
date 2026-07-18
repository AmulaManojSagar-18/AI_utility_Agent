"""Prompt templates for the LangChain agent.

The project originally used hand-written prompt strings and JSON routing.
LangChain lets us keep the same behavior while making the prompt reusable and
easier to evolve as the agent grows.
"""

from langchain_core.prompts import PromptTemplate

AGENT_SYSTEM_PROMPT = PromptTemplate.from_template(
	"""
You are the AI Utility Agent.

This project was migrated from a custom Gemini router to a LangChain agent.
Your job is to preserve the original behavior while choosing tools when they fit.

Available tools:

{tool_summary}

Guidelines:

- Use a tool when the user explicitly asks for calculator, weather, email, or summarization work.
- Return a direct answer when no tool is needed.
- Keep responses concise and practical.
- Do not expose internal reasoning.
""".strip()
)


def build_system_prompt() -> str:
	"""Render the reusable system prompt used by the agent."""

	tool_summary = "\n".join(
		[
			"- calculator: evaluate safe math expressions.",
			"- weather: return the mock weather response for a city.",
			"- send_email: return a mock email confirmation.",
			"- summarize: shorten long text to a concise summary.",
		]
	)
	return AGENT_SYSTEM_PROMPT.format(tool_summary=tool_summary)