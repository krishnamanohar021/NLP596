import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

HEADERS = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get("https://api.example.com/sata", headers=HEADERS)
print(response.json())


