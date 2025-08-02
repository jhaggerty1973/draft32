import feedparser
import re

TICKER_PATTERN = re.compile(r"\$?[A-Z]{2,5}")

def query_top_meme_stocks():
    url = "https://news.google.com/rss/search?q=top+meme+stocks"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries]
    tickers = []
    for title in headlines:
        matches = TICKER_PATTERN.findall(title.upper())
        tickers.extend([m.replace("$", "") for m in matches if m.isalpha()])
    return list(set(tickers))[:10]