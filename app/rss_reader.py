import feedparser
from urllib.parse import quote

# 除外するメディアのリスト
excluded_sources = [
    "Full-Count",
    "東スポ",
    "ライブドア",
    "THE DIGEST",
    "オリコンニュース",
    "デイリースポーツ",
    "ジアンサー",
    "女性自身",
    "ハフポスト日本版",
]


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
        # エントリーのソース名を取得
        source_title = entry.get("source", {}).get("title", "")

        # 除外するメディアに含まれていない場合のみ追加
        if not any(excluded_source in source_title for excluded_source in excluded_sources):
            news = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "source": source_title,
            }
            news_list.append(news)

    return news_list


# 実際の利用例
if __name__ == "__main__":
    keyword = "プロ野球"
    articles = fetch_news(keyword)
    for article in articles:
        print(f"Title: {article['title']} - Source: {article['source']}")
