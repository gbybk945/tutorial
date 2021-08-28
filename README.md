# tutorial

## このアプリについて

ブログ記事を管理するためのアプリ

※Flask チュートリアルの練習用リポジトリ

https://study-flask.readthedocs.io/ja/latest/02.html

## Usage(使い方)
### requirements.txtについて
- ブログアプリに必要なライブラリをインストールするためのテキストコード
```
$ pip install -r requirements.txt
```
をターミナルで起動しインストール

### manage.pyについて
- flaskrというアプリを起動し実行するためのファイル
```
from flaskr import app
app.run(host='127.0.0.1', port=5000, debug=True)
```

### flaskr/__init__.pyについて
- ブログアプリを作成するため、データベースを仕様できるようにする初期設定
```
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

import flaskr.views
```

### flaskr/config.pyについて
- SQLiteというデータベースを使い、ファイル名を指定してデータベース管理する。また、セッション情報を暗号化するためのキーの設定。
※実際に運用する場合は変更が必要。
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskr.db'
SECRET_KEY = 'secret key'
```

### flaskr/models.pyについて
- ブログの記事（データ）を格納するデータベースを作成
```
from flaskr import db

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
                id=self.id, title=self.title)

def init():
    db.create_all()
```
作成したデータベース定義を読み込み、データベースファイルを作成する。
```
$ python3
>>> from flaskr.models import init
>>> init()
```
flaskr/flaskr.dbが生成されたら動作確認
```
$ python3
>>> from flaskr.models import Entry, db
>>> Entry.query.all()
[]
>>> entry = Entry(title='title', text='text')
>>> db.session.add(entry)
>>> db.session.commit()
>>> Entry.query.all()
[<Entry id=1 title=u'title'>]

>>> entry = Entry.query.get(1)
>>> entry
<Entry id=1 title=u'title'>
>>> entry.title = 'Hello world'
>>> db.session.add(entry)
>>> db.session.commit()
>>> Entry.query.all()
[<Entry id=1 title=u'Hello world'>]

>>> entry = Entry.query.filter(Entry.title == 'Hello world').first()
>>> entry
<Entry id=1 title=u'Hello world'>
>>> db.session.delete(entry)
>>> db.session.commit()
>>> Entry.query.all()
[]
```
### flaskr/views.pyについて
- ページを表示する。また、記事の情報をデータベースに追加・格納する機能を持つ。
- 関連コード・・・show_entries.html,layout.html,style.css
```
from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import Entry

@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
```
flaskr/template/layout.html
```
<!doctype html>
<title>Flaskr</title>
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
<div class=page>
  <h1>Flaskr</h1>
  {% for message in get_flashed_messages() %}
    <div class=flash>{{ message }}</div>
  {% endfor %}
  {% block body %}{% endblock %}
</div>
```
flaskr/templates/show_entries.html
```
{% extends "layout.html" %}
{% block body %}
  <form action="{{ url_for('add_entry') }}" method=post class=add-entry>
    <dl>
      <dt>Title:
      <dd><input type=text size=20 name=title>
      <dt>Text:
      <dd><textarea name=text rows=5 cols=20></textarea>
      <dd><input type=submit value=Share>
    </dl>
  </form>

  <ul class=entries>
  {% for entry in entries %}
    <li><h2>{{ entry.title }}</h2>{{ entry.text|safe }}
  {% else %}
    <li><em>Unbelievable.  No entries here so far</em>
  {% endfor %}
  </ul>
{% endblock %}
```
flaskr/static/style.css
```
body            { font-family: sans-serif; background: #eee; }
a, h1, h2       { color: #377ba8; }
h1, h2          { font-family: 'Georgia', serif; margin: 0; }
h1              { border-bottom: 2px solid #eee; }
h2              { font-size: 1.2em; }

.page           { margin: 2em auto; width: 35em; border: 5px solid #ccc;
                  padding: 0.8em; background: white; }
.entries        { list-style: none; margin: 0; padding: 0; }
.entries li     { margin: 0.8em 1.2em; }
.entries li h2  { margin-left: -1em; }
.add-entry      { font-size: 0.9em; border-bottom: 1px solid #ccc; }
.add-entry dl   { font-weight: bold; }
.metanav        { text-align: right; font-size: 0.8em; padding: 0.3em;
                  margin-bottom: 1em; background: #fafafa; }
.flash          { background: #cee5F5; padding: 0.5em;
                  border: 1px solid #aacbe2; }
.error          { background: #f0d6d6; padding: 0.5em; }
```

## 動作確認
```
python manage.py
```
http://127.0.0.1:5000 をブラウザで開いて動作を確認。

## 画面レイアウト
![チュートリアル](c4fd868b-38c6-453d-b058-37c614a8be2f(1).png)


## その他
- セッション情報を暗号化するためのキーの設定について、実際に運用する場合は変更が必要。