import feedparser
from urllib.parse import quote


def fetch_news(keyword):
    # クエリパラメータをエンコード
    encoded_keyword = quote(keyword)
    # Google NewsのRSSフィードURL
    feed_url = f"https://news.google.com/rss/search?q={encoded_keyword}&hl=ja&gl=JP&ceid=JP:ja"

    # フィードをパース
    feed = feedparser.parse(feed_url)

    # ニュースのリストを作成
    news_list = []
    for entry in feed.entries:
        news = {"title": entry.title, "link": entry.link, "published": entry.published}
        news_list.append(news)

    return news_list
