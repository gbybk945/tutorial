# tutorial

## このアプリについて

ブログ記事を管理するためのアプリ

※Flask チュートリアルの練習用リポジトリ

https://study-flask.readthedocs.io/ja/latest/02.html

## Usage(使い方)


### manage.pyについて
- flaskrというアプリを起動し実行するためのファイル
### requirements.txtについて
- ブログアプリに必要なライブラリをインストールするためのテキストコード
```
$ pip install -r requirements.txt
```
をターミナルで起動しインストール

### __init__.pyについて
- ブログアプリを作成するため、データベースを仕様できるようにする初期設定

### config.pyについて
- SQLiteというデータベースを使い、ファイル名を指定してデータベース管理する。また、セッション情報を暗号化するためのキーの設定。
※実際に運用する場合は変更が必要。

### models.pyについて
- ブログの記事（データ）を格納するデータベースを作成

### views.pyについて
- ページを表示する。また、記事の情報をデータベースに追加・格納する機能を持つ。
- 関連コード・・・show_entries.html,layout.html,style.css

## その他
- oo は完全に完成していません