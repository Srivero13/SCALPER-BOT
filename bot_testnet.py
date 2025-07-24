from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import time
import threading
import random
api_key = 'YOUR_KEY'
api_secret = 'YOUR_SECRET'
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'
symbol = 'BTCUSDT'
trade_quantity = 0.0005 
def should_buy():
    return random.choice([True, False])
def place_buy_order():
    try:
        order = client.create_order(
            symbol=symbol,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=trade_quantity
        )
        print("COMPRA ejecutada:", order['fills'])
        return True
    except BinanceAPIException as e:
        print("Error al comprar:", e)
        return False
def place_sell_order():
    try:
        order = client.create_order(
            symbol=symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=trade_quantity
        )
        print("VENTA ejecutada:", order['fills'])
        return True
    except BinanceAPIException as e:
        print("Error al vender:", e)
        return False
def run_scalping():
    while True:
        if should_buy():
            place_buy_order()
            time.sleep(2)
            place_sell_order()
        else:
            place_sell_order()
            time.sleep(2)
            place_buy_order()
        time.sleep(5)
for i in range(5):
    t = threading.Thread(target=run_scalping)
    t.daemon = True
    t.start()
print("Scalper iniciado con 5 hilos en Binance Testnet...")
while True:
    time.sleep(1)
