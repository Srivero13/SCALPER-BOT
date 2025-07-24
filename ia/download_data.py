from binance.client import Client
import pandas as pd
import time
import datetime
API_KEY = 'YOUR_KEY'
API_SECRET = 'YOUR_SECRET'
client = Client(API_KEY, API_SECRET)
symbol = "BTCUSDT"
interval = Client.KLINE_INTERVAL_1MINUTE
start_date = "1 Jan, 2024"
end_date = "1 Jul, 2024"
print("Descargando datos...")
klines = client.get_historical_klines(symbol, interval, start_date, end_date)
df = pd.DataFrame(klines, columns=[
    "timestamp", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "num_trades",
    "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
])
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df = df[["timestamp", "open", "high", "low", "close", "volume"]]
df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
df.to_csv("historical_data.csv", index=False)
print("Datos guardados como historical_data.csv")
