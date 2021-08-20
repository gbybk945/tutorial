# ブログの記事（データ）を格納するデータベースを作成

from flaskr import db # データベースをインポート

class Entry(db.Model): # dbのModelを継承したテーブルのクラスを定義
    __tablename__ = 'entries' # テーブル名を設定
    id = db.Column(db.Integer, primary_key=True) # カラムの設定　記事のid（テーブルの主キー）
    title = db.Column(db.Text) # カラムの設定　記事のタイトル名
    text = db.Column(db.Text) # カラムの設定　記事の内容

    def __repr__(self): #Entryクラスのインスタンスが生成された際、<Entry id={id} title={title!r}>の文字列を返す
        return '<Entry id={id} title={title!r}>'.format(
                id=self.id, title=self.title)

def init(): # データベースの枠組みを作成する（この時点で値は入っていない）
    db.create_all()
