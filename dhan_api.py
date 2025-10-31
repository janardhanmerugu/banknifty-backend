import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
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
