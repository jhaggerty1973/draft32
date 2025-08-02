import subprocess
import json

def scrape_tweets(limit=50):
    query = "($GME OR AMC OR BBBY OR TSLA OR AAPL) lang:en"
    cmd = f'snscrape --jsonl --max-results {limit} twitter-search "{query}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    tweets = []
    for line in result.stdout.splitlines():
        data = json.loads(line)
        tweets.append({"source": "twitter", "title": data["content"]})
    return tweets