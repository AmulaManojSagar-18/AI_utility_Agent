"""CLI entry point for the AI Utility Agent."""

from agent import run_agent
from memory import SESSION_ID


def main() -> None:
    """Run the interactive chat loop."""

    print("AI Utility Agent is running. Type 'exit' to quit.")
    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if user.lower() == "exit":
            break

        if not user:
            continue

        answer = run_agent(user, session_id=SESSION_ID)
        print(answer)


if __name__ == "__main__":
    main()