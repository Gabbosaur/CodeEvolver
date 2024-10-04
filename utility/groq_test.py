import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You're an expert Java developer. "
        },
        {
            "role": "user",
            "content": "Tell me about cats",
        }
    ],
    model="llama-3.1-8b-instant",
)

print(chat_completion.choices[0].message.content)