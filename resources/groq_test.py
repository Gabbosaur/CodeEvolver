import os

from groq import Groq

def remove_multiple_newlines(input_string: str) -> str:
    # Use regex to replace multiple newlines with a single newline
    return re.sub(r'\n+', '\n', input_string).strip()

def to_pascal_case(s: str) -> str:
    # Split the string by spaces or underscores and capitalize each word
    return ''.join(word.capitalize() for word in s.replace('_', ' ').split())

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