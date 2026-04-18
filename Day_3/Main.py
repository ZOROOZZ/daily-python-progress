from fastapi import FastAPI

# 1. Initialize the API app
app = FastAPI()

# 2. Your exact data
market_data = [
    {"ticker": "AAPL", "price": 150, "trend": "up"},
    {"ticker": "TSLA", "price": 200, "trend": "down"},
    {"ticker": "GOOG", "price": 130, "trend": "up"}
]

# 3. Create an "endpoint". When someone visits the "/analyze" URL, this function runs.
@app.get("/analyze")
def analyze_stocks():
    
    # The empty bucket to hold our results
    results = []
    
    # Your exact loop
    for stock in market_data:
        if stock["trend"] == "up":
            results.append(f"{stock['ticker']} is going up!")
        elif stock["trend"] == "down":
            results.append(f"{stock['ticker']} is going down!")
            
    # 4. Return the data as a dictionary (this automatically turns into JSON for the web)
    return {"status": "success", "data": results}
    