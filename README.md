# SCALPER-BOT

**SCALPER-BOT** is a fully automated trading bot designed for high-frequency scalping on the BTC/USDT pair using Binance Futures Testnet. It integrates real-time order execution, market data analysis, risk management via stop-loss, and a machine learning model trained on historical market data.

## Features

- High-frequency scalping strategy
- Machine learning model for entry prediction
- Integration with Binance Futures Testnet
- Real-time order book and price monitoring
- Risk control with dynamic stop-loss
- Modular code structure for clarity and maintenance

## Requirements

- Python 3.8 or higher
- A Binance Testnet Futures account
- Python libraries:
  - `python-binance`
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `joblib`
  - `matplotlib`
  - `requests`

Install all dependencies:

```bash
pip install -r requirements.txt
SCALPER-BOT/
├── bot_testnet.py            # Main scalping bot using testnet
├── monitor.py                # Real-time trade monitor and balance display
├── download_data.py          # Historical market data downloader (via Binance API)
├── generate_dataset.py       # Feature engineering and dataset generation
├── train_model.py            # Model training and saving
├── keys_testnet.py           # Your testnet API keys (excluded from version control)
├── final_dataset.csv         # Output dataset used for model training
├── model.pkl                 # Trained model file
└── requirements.txt
```
Binance Testnet Setup
Create an account at: https://testnet.binancefuture.com

Go to "API Management" and generate a new API key.

Enable the following permissions:

Enable Futures

Enable Reading

Disable IP restrictions during development

Save your API keys in a file named keys_testnet.py:

python
Copy
Edit
API_KEY = 'your_testnet_api_key'
API_SECRET = 'your_testnet_secret_key'
Usage
1. Download Historical Data
bash
Copy
Edit
python download_data.py
2. Generate Dataset
bash
Copy
Edit
python generate_dataset.py
3. Train the Model
bash
Copy
Edit
python train_model.py
The model will be saved as model.pkl.

4. Run the Bot (Testnet)
bash
Copy
Edit
python bot_testnet.py
5. Monitor Live Performance (Optional)
bash
Copy
Edit
python monitor.py
This script will display wallet balance, last executed trades, and market price updates.

Notes
The model is trained on simple features and should be improved for real-world usage.

This bot is configured for Binance Testnet only and will not execute real trades.

The ORDER_TYPE_STOP_MARKET constant must be handled manually depending on the version of the Binance API library; alternatively, use the string "STOP_MARKET" directly.

Disclaimers
This project is intended for educational and research purposes only. Use at your own risk. The authors are not responsible for any financial losses or misuse of this code in production environments.
