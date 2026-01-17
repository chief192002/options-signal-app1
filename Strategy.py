import ta

def generate_signal(df):
    df['ema9'] = ta.trend.EMAIndicator(df['Close'], 9).ema_indicator()
    df['ema21'] = ta.trend.EMAIndicator(df['Close'], 21).ema_indicator()
    df['rsi'] = ta.momentum.RSIIndicator(df['Close'], 14).rsi()
    macd = ta.trend.MACD(df['Close'])
    df['macd_hist'] = macd.macd_diff()

    last = df.iloc[-1]

    if last['ema9'] > last['ema21'] and last['rsi'] > 55 and last['macd_hist'] > 0:
        return "CALL"

    if last['ema9'] < last['ema21'] and last['rsi'] < 45 and last['macd_hist'] < 0:
        return "PUT"

    return "NO TRADE"
