#!/bin/python3
from binance.client import Client
import time
import os

api_key = "vZCzPXIIhkBH9XObfMbIJoyoguB55VIfD85xdzbOrLREqBNuPgXKWeCdkrIGOacZ"
api_secret = "kpLJOxigXpjTA4vc3abqturOZ2zlEZdXOLKyJyvNUSWG3uCbIoSCN3N6kRn6Er3J"

client = Client(api_key, api_secret)

investors = {
    "Jake": {
        "price": 4500,
        "coins": 11504.66
    },
    "Damo": {
        "price": 106.92,
        "coins": 734.34
    }
}


multiple_investors = len(investors) > 1

while True:
    symbol_ticker = client.get_symbol_ticker(symbol="DOGEAUD")

    if multiple_investors:
        os.system("clear")

    for name, investor in investors.items():
        doge_price = float(symbol_ticker["price"])
        new_balance = round(doge_price * investor["coins"], 2)
        profit = round(new_balance - investor["price"], 2)
        profit_percent = round(profit / investor["price"] * 100, 2)

        if multiple_investors:
            print(name + ":")
            print(f"    Investment: {investor['price']}")
            print(f"    Current value: {new_balance}")
            print(f"    Profit: {profit} ({profit_percent}%)")
        else:
            print(f"{investor['price']} -> {new_balance} = {profit} ({profit_percent}%)")

    time.sleep(5)