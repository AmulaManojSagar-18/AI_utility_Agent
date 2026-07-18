import json

from gemini_client import ask_gemini

from tools import (
    calculator,
    weather,
    send_email,
    summarize
)

def run_agent(user_input):

    response = ask_gemini(user_input)

    decision = json.loads(response)

    tool = decision["tool"]

    if tool == "calculator":
        return calculator(decision["input"])

    elif tool == "weather":
        return weather(decision["city"])

    elif tool == "send_email":
        return send_email(
            decision["receiver"],
            decision["message"]
        )

    elif tool == "summarize":
        return summarize(decision["text"])

    else:
        return decision["answer"]