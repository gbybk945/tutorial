# flaskrというアプリを起動し実行するためのファイル
# appは__init__.pyにてflaskモジュールのFlaskクラスから生成したインスタンス
from flaskr import app 

# ローカルサーバーを起動し、アプリを立ち上げるためのメソッド
app.run(host='127.0.0.1', port=5000, debug=True)