from anthropic import anthropic
from config import CLAUDE_API_KEY

client = Anthropic(api_key=CLAUDE_API_KEY)

def call_claude(prompt: str):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
        
    )
    return response.content[0].text