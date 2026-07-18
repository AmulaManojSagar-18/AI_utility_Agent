import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import SYSTEM_PROMPT

# Load variables from .env
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load the model
model = genai.GenerativeModel("gemini-3.1-flash-lite")


def ask_gemini(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text



def ask_gemini(user_prompt):

    prompt = f"""
{SYSTEM_PROMPT}

User:
{user_prompt}
"""

    response = model.generate_content(prompt)

    return response.text