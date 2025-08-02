from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(posts):
    analyzer = SentimentIntensityAnalyzer()
    for post in posts:
        score = analyzer.polarity_scores(post["title"])
        post["sentiment"] = score["compound"]
    return posts