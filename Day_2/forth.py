market_data = [
    {"ticker": "AAPL", "price": 150, "trend": "up"},
    {"ticker": "TSLA", "price": 200, "trend": "down"},
    {"ticker": "GOOG", "price": 130, "trend": "up"}
]
def analyze_stocks(market_data):
    
    for stock in market_data:
        if stock:
            print(f"[Ticker] is going up!")
        else:
            print(f"[Ticker] is going down!")