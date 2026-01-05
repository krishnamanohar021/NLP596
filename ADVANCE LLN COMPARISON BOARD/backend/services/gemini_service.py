import google.generativeai as genai 
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def call_gemini(prompt: str);
model = genai.generativeModel("gemini-1.5-falsh")
response = model.generative_content(prompt)
return response.text