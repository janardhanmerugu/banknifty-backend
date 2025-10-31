import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzYxOTg3MDc3LCJpYXQiOjE3NjE5MDA2NzcsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTA5MDIwNDgyIn0.kUg6PuC7YT9KfrL7DoCC7oHwCHKk8wmCsFFa5NO8on8qXyd6Z37z1r058dyvRHyt6QesOi8kF2B-xK4HyDzW9g")
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
BASE_URL = "https://api.dhan.co/v2"

def get_banknifty_quote():
    headers = {
        "access-token": ACCESS_TOKEN,
        "dhanClientId": CLIENT_ID,
        "accept": "application/json"
    }
    url = f"{BASE_URL}/marketfeed/quote/26009"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text, "status": response.status_code}
