import time
import numpy as np
from binance.client import Client
from binance.enums import *
from config import *
import pandas as pd
import ta
from joblib import load
from utils import get_order_book, calculate_pressure
from joblib import load
model = load("model.pkl")
client = Client(API_KEY, API_SECRET)
client.API_URL = 'https://testnet.binance.vision/api'
last_trade_time = 0
def should_enter_trade(price_history):
    close_series = pd.Series(price_history)
    rsi = ta.momentum.RSIIndicator(close=close_series, window=14).rsi().iloc[-1]
    ema = ta.trend.EMAIndicator(close=close_series, window=9).ema_indicator().iloc[-1]
    features = [[rsi, ema]]
    prediction = model.predict(features)
    return prediction[0] == 1
def execute_trade(current_price):
    global last_trade_time
    if time.time() - last_trade_time < MIN_INTERVAL:
        return
    qty = round(QUANTITY_USDT / current_price, 6)
    try:
        buy = client.create_order(
            symbol=PAIR,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=qty
        )
        entry_price = float(buy['fills'][0]['price'])
        print(f"Comprado a {entry_price}")
        stop_loss = round(entry_price * (1 - STOP_LOSS_PCT), 2)
        take_profit = round(entry_price * (1 + TAKE_PROFIT_PCT), 2)
        while True:
            price = float(client.get_symbol_ticker(symbol=PAIR)['price'])
            if price <= stop_loss:
                client.create_order(symbol=PAIR, side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity=qty)
                print(f"Stop Loss activado a {price}")
                break
            elif price >= take_profit:
                client.create_order(symbol=PAIR, side=SIDE_SELL, type=ORDER_TYPE_MARKET, quantity=qty)
                print(f"Take Profit activado a {price}")
                break
            time.sleep(0.5)
        last_trade_time = time.time()
    except Exception as e:
        print(f"Error en la operación: {e}")
def main():
    price_history = []
    print("Bot iniciado...")
    while True:
        try:
            price = float(client.get_symbol_ticker(symbol=PAIR)['price'])
            price_history.append(price)

            if len(price_history) > 50:
                price_history.pop(0)

                bids, asks = get_order_book(client)
                pressure = calculate_pressure(bids, asks)

                if pressure > 0.1 and should_enter_trade(price_history):
                    execute_trade(price)
            time.sleep(0.3) 
        except Exception as e:
            print(f"Error general: {e}")
            time.sleep(2)
if __name__ == "__main__":
    main()
