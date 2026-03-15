import os
import httpx
from dotenv import load_dotenv

load_dotenv("backend/.env")
key = os.getenv("GEMINI_API_KEY")

r = httpx.get(f"https://generativelanguage.googleapis.com/v1beta/models?key={key}")
models = r.json().get("models", [])

for m in models:
    if "flash" in m["name"].lower() or "gemini" in m["name"].lower():
        print(f"- {m['name']}")
