from agent import run_agent

while True:

    user = input("You: ")

    if user=="exit":
        break

    answer = run_agent(user)

    print(answer)