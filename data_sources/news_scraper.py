import feedparser

def get_news_articles(ticker):
    query = f"{ticker}+stock"
    url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries]
    return "; ".join(headlines[:3]) if headlines else "No recent headlines"