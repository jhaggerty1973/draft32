import requests

def scrape_reddit_posts(limit=50):
    url = f"https://api.pushshift.io/reddit/search/submission/?subreddit=wallstreetbets&sort=desc&sort_type=created_utc&size={limit}"
    res = requests.get(url)
    posts = res.json().get("data", [])
    return [{"source": "reddit", "title": post.get("title", "")} for post in posts if post.get("title")]