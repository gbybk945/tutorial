#ブログアプリを作成するため、データベースを仕様できるようにする初期設定

#flaskのモジュール（Flaskクラス）をインポート
from flask import Flask　
#データベースとやりとりをするライブラリをインポート
#SQLの文を書かずにSQLAlchemyのライブラリが持っている関数を利用する事で代わりにSQL文の生成が可能。
from flask_sqlalchemy import SQLAlchemy　

app = Flask(__name__)　#Flaskのインスタンスを生成して変数appに割り当て
app.config.from_object('flaskr.config')　#pythonオブジェクトであるflaskr.configを読み込み、appの設定（config.pyで設定）を追加

#SQLAlchemyのインスタンスを生成し変数dbに割り当て。
#引数にFlaskのインスタンス（app）を渡すことで、FlaskでSQLAlchemyを利用してデータベースを扱うようにできる。
db = SQLAlchemy(app)　

import flaskr.views　#views.pyモジュールをインポート