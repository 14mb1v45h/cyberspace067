import requests
import pandas as pd

def get_portfolio_value(coins):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(coins), "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    prices = response.json()
    portfolio = {"Coin": [], "Price": []}
    for coin in coins:
        portfolio["Coin"].append(coin)
        portfolio["Price"].append(prices[coin]["usd"])
    return pd.DataFrame(portfolio)

coins = ["bitcoin", "ethereum", "ripple"]  # Add your coins
print(get_portfolio_value(coins))