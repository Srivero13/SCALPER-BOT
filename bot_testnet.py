from binance.client import Client
from binance.exceptions import BinanceAPIException
import joblib
import numpy as np
import time
import threading
import requests
from keys_testnet import API_KEY, API_SECRET
#SETTINGS
symbol = 'BTCUSDT'
quantity = 0.0005
INTERVALO = 5
#BINANCE
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
#AI
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
#MARKET
def get_latest_features():
    url = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval=1m&limit=2"
    try:
        data = requests.get(url).json()
        if len(data) < 2:
            return None
        precio_actual = float(data[-1][4])
        precio_anterior = float(data[-2][4])
        volumen = float(data[-1][5])
        cambio_pct = (precio_actual - precio_anterior) / precio_anterior
        volumen_norm = min(volumen / 100, 1)
        scaled = scaler.transform([[cambio_pct, volumen_norm]])
        return scaled, precio_actual
    except Exception as e:
        print("Error obteniendo datos de mercado:", e)
        return None
#TRADING
def place_order(side):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"{side} ejecutado:", order)
        return True
    except BinanceAPIException as e:
        print(f"Error en orden {side}:", e)
        return False
#SCALPING LOOP
def scalping_loop():
    while True:
        features_data = get_latest_features()
        if not features_data:
            time.sleep(INTERVALO)
            continue
        features_scaled, current_price = features_data
        pred = model.predict(features_scaled)[0]
        if pred == 1:
            print(f"[IA] Predicción COMPRA a {current_price} USDT")
            place_order("BUY")
            time.sleep(2)
            place_order("SELL")
        else:
            print(f"[IA] Predicción VENTA a {current_price} USDT")
            place_order("SELL")
            time.sleep(2)
            place_order("BUY")
        time.sleep(INTERVALO)
#Threading
for i in range(5):
    hilo = threading.Thread(target=scalping_loop)
    hilo.daemon = True
    hilo.start()
print("Scalping bot iniciado con IA y 5 hilos en Binance Futures Testnet...")
while True:
    time.sleep(1)
