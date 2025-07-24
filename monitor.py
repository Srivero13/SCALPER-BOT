from binance.client import Client
API_KEY = 'YOUR_KEY'
API_SECRET = 'YOUR_SECRET'
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
try:
    balance = client.futures_account_balance()
    print("API key válida. Tu balance en la testnet es:\n")
    for asset in balance:
        print(f"{asset['asset']}: {asset['balance']}")
except Exception as e:
    print("Error al verificar claves API:")
    print(e)
