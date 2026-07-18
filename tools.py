def calculator(expression: str):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Invalid Expression"
    
def weather(city):
    return f"It is currently sunny in {city} with 31°C."

def send_email(receiver, message):
    return f"Email sent to {receiver} with message: {message}"

def summarize(text):
    words = text.split()

    if len(words) <= 20:
        return text

    return " ".join(words[:20]) + "..."