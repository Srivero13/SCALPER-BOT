from binance.client import Client
import numpy as np
def get_order_book(client, symbol='BTCUSDT', depth=10):
    book = client.get_order_book(symbol=symbol, limit=depth)
    bids = np.array([[float(bid[0]), float(bid[1])] for bid in book['bids']])
    asks = np.array([[float(ask[0]), float(ask[1])] for ask in book['asks']])
    return bids, asks
def calculate_pressure(bids, asks):
    bid_volume = np.sum(bids[:, 1])
    ask_volume = np.sum(asks[:, 1])
    return (bid_volume - ask_volume) / (bid_volume + ask_volume)
