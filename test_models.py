import os
import httpx
from dotenv import load_dotenv

load_dotenv("backend/.env")
key = os.getenv("GEMINI_API_KEY")

models_to_test = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-2.5-flash",
    "gemini-1.5-flash-latest"
]

for model in models_to_test:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    payload = {"contents": [{"parts": [{"text": "hi"}]}]}
    r = httpx.post(url, json=payload)
    print(f"Model: {model} -> Status: {r.status_code}")
    if r.status_code == 200:
        print("  OK Works!")
    else:
        try:
            err = r.json()
            msg = err.get("error", {}).get("message", r.text)[:150]
            print(f"  FAIL {msg}")
        except:
            print(f"  FAIL {r.text[:150]}")
