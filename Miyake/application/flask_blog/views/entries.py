#views.pyから派生、新しい投稿に関する動きはこっちで指定
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog.models.entries import Entry
from flask_blog import db #テキストp147

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login') #ログインしていない場合には、ログイン画面に自動で遷移する
        #return redirect(url_for('login')) #自動でリンクを作成（ｐ114)
    entries = Entry.query.order_by(Entry.id.desc()).all() #データベースから生地を取得し新しい順に並べる（ｐ152）
    return render_template('entries/index.html', entries=entries) #データベースから取得したすべての記事がentriesの名前で参照できる
    #return render_template('entries/index.html')

@app.route('/entries',methods=['POST'])  #投稿内容を受信し、データベースに保存する処理
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry) #entryの内容をデータベースに保存
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')

@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)
