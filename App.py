from fastapi import FastAPI
from data import get_data
from strategy import generate_signal

app = FastAPI(title="Options Signal App")

symbols = ["TSLA", "SPY", "QQQ"]

@app.get("/")
def signals():
    results = {}
    for symbol in symbols:
        df = get_data(symbol)
        results[symbol] = generate_signal(df)
    return results
