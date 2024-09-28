from flask import Flask

app = Flask(__name__, template_folder="../templates")  # 必要な場合にのみ設定


# ルートをインポートしてアプリケーションに登録
from app import routes
