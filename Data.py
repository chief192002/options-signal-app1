import yfinance as yf

def get_data(symbol):
    return yf.download(
        symbol,
        interval="5m",
        period="5d",
        progress=False
    )
