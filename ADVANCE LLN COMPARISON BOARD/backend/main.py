import asyncio
from fastapi import fastapi
from models import PromptRequest
from services.openai_service import call_openai
from services.gemini_service import call_gemini
from services.claude_service import call_claude

app = FastAPI(title="LLM Comparison API")

@app.post9("/compare")
async def compare_llms(data: PromptRequest):
    prompt = data.prompt

    loop = asyncio.get_event_loop()

    openai_task = loop.run_in_executor(None, call_openai, prompt)
    gemini_task = loop.run_in_executor(None, call_gemini,prompt)
    claude_task = loop.run_in_executor(None, call_claude,prompt)

    openai_res,gemini_res,claude_res = await asyncio.gather(
        openai_task,gemini_task, claude_task

    )

    return{
        "OpenAI": openai_res,
        "Gemini": gemini_res,
        "claude": claude_res
    }