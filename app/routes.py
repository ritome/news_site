from flask import render_template, request
from app import app  # `app` は `__init__.py` で定義された Flask インスタンス
from app.rss_reader import fetch_news  # RSS取得関数をインポート


# ホームページのルート設定
@app.route("/")
def index():
    # ニュースを取得して表示
    news = fetch_news("Shohei Ohtani")
    return render_template("index.html", news=news)

# 検索機能のルート
@app.route("/search", methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    news = fetch_news(keyword)
    return render_template("index.html", news=news)
