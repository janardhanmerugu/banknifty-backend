from fastapi import FastAPI
from dhan_api import get_banknifty_quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "BankNifty Mock Trader Backend Active"}

@app.get("/banknifty")
def banknifty_quote():
    data = get_banknifty_quote()
    return data
