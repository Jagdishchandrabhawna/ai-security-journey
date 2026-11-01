from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "You are SahayakBot, a polite Indian bank assistant."},
        {"role": "user", "content": "Give me 3 tips to avoid UPI fraud."},
    ],
)
print(response.message.content)