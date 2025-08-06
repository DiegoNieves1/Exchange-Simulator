import json
import os
from datetime import datetime

LOG_FILE = "price_log.json"

def load_price_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_price_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=4)

def log_prices(prices: dict):
    timestamp = datetime.now().isoformat()
    log = load_price_log()

    for symbol, info in prices.items():
        if "price" in info:
            entry = {
                "price": float(info["price"]),
                "timestamp": timestamp
            }
            if symbol not in log:
                log[symbol] = []
            log[symbol].append(entry)

    save_price_log(log)