from flask import request, redirect, url_for, render_template, flash # flaskのライブラリをインポート
from flaskr import app, db # Flaskのインスタンス（app）,データベースのインスタンス（db）をインポート
from flaskr.models import Entry # modelsモジュールのEntryクラスをインポート

@app.route('/') # http://127.0.0.1:5000/でアクセスしてきた場合、show_entries()を実行してshow_entries.htmlを表示する
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

# http://127.0.0.1:5000/addでアクセスしてきた場合、add_entry()を実行してデータベースに内容を追加。
# その後New entry was successfully postedというメッセージを表示し、show_entries.htmlを表示する。
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
