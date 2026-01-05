import os 
from dotenv import load_dotenv

load_dotenev()

OPENAI_API_KEY = os.getenev("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")