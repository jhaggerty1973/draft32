import re
import random
import pandas as pd

TICKER_PATTERN = re.compile(r"\$?\b[A-Z]{2,5}\b")

def mock_price_lookup(ticker):
    return round(random.uniform(1.0, 200.0), 2)

def extract_and_aggregate(posts):
    counts = {}
    for post in posts:
        matches = TICKER_PATTERN.findall(post["title"].upper())
        for ticker in matches:
            if not ticker.isalpha(): continue
            if ticker not in counts:
                counts[ticker] = {"mentions": 0, "sentiment_sum": 0.0}
            counts[ticker]["mentions"] += 1
            counts[ticker]["sentiment_sum"] += post["sentiment"]

    rows = []
    for ticker, data in counts.items():
        avg_sentiment = data["sentiment_sum"] / data["mentions"]
        price = mock_price_lookup(ticker)
        signal = "BUY" if avg_sentiment > 0.6 and price < 50 else "HOLD"
        rows.append({
            "Ticker": ticker,
            "Total Mentions": data["mentions"],
            "Avg Sentiment": round(avg_sentiment, 2),
            "Current Price": price,
            "Signal": signal
        })

    if rows:
        return pd.DataFrame(rows, columns=["Ticker", "Total Mentions", "Avg Sentiment", "Current Price", "Signal"])
    else:
        return pd.DataFrame(columns=["Ticker", "Total Mentions", "Avg Sentiment", "Current Price", "Signal"])