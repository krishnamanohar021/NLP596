import asyncio
from fastapi import fastapi
from fastapi.middleware.cors import CORSMiddleware
from models import PromptRequest
from services.openai_service import call_openai
from services.claude_service import call_claude
from services.gemini_service import call_gemini

app = FastAPI()

app.add_middleware(
    CORSMiddleware
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/compare")
async def compare_llms(data: PromptRequest):
    prompt = data.prompt

    results = await asyncio.gather(
        call_openai(prompt),
        call_claude(prompt),
        call_gemini(prompt)
    )

    return {
        "OpenAI": results[0],
        "claude": results[1],
        "Gemini": results[2]
    }