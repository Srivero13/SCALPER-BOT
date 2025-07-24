import pandas as pd
import ta
df = pd.read_csv("historical_data.csv")
df["rsi"] = ta.momentum.RSIIndicator(close=df["close"], window=14).rsi()
df["ema"] = ta.trend.EMAIndicator(close=df["close"], window=9).ema_indicator()
df["return_1m"] = df["close"].pct_change().shift(-1)
df["target"] = (df["return_1m"] > 0).astype(int)
df = df.dropna()
df.to_csv("final_dataset.csv", index=False)
print("Dataset enriquecido guardado como final_dataset.csv")
