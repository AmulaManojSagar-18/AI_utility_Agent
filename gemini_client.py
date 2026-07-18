"""Gemini model setup for the LangChain agent.

The old project called the Gemini SDK directly. LangChain centralizes model
configuration here so the rest of the app can work with a standard chat model
interface.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment or .env file.")


def get_chat_model() -> ChatGoogleGenerativeAI:
    """Create the Gemini chat model used by the LangChain agent."""

    return ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        api_key=API_KEY,
        temperature=0,
    )