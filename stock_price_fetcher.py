import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Replace this with your actual Twelve Data API key
API_KEY = os.getenv("TWELVE_DATA_API_KEY")
tickers =["NVDA"]

def fetch_prices(symbols):
    symbol_str = ",".join(symbols)
    url = f"https://api.twelvedata.com/price?symbol={symbol_str}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Normalize to always return a dict of {symbol: {price: ...}}
    if len(symbols) == 1:
        if isinstance(data, dict) and "price" in data:
            return {symbols[0]: data}
        elif isinstance(data, dict) and "message" in data:
            return {symbols[0]: data}  # Return the error as-is
        else:
            return {symbols[0]: {"message": str(data)}}
    return data

if __name__ == "__main__":
    prices = fetch_prices(tickers)
    
    for symbol, info in prices.items():
        if "price" in info:
            print(f"{symbol}: ${info['price']}")
        else:
            print(f"{symbol}: Error - {info.get('message', 'Unknown error')}")
