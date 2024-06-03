from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps

# ↓の部分：entries.pyに移した
# @app.route('/')
# def show_entries():
#     if not session.get('logged_in'):
#         return redirect('/login') #ログインしていない場合には、ログイン画面に自動で遷移する
#         #return redirect(url_for('login')) #自動でリンクを作成（ｐ114）
#     return render_template('entries/index.html')         

def login_required(view): #テキストｐ189　デコレータを作る
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            #print('ユーザ名が異なります') #ターミナルへの表示（webページには表示されない）
            flash('ユーザ名が異なります') #webページへの表示、ユーザにメッセージが表示される
        elif request.form['password'] != app.config['PASSWORD']:
            #print('パスワードが異なります')
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True #変数session中のlogged_inの値をTrueにセット　→　この値をリクエストのたびチェックすることでログインしているか判別する
            flash('ログインしました')
            return redirect('/')
            #return redirect(url_for('show_entries'))
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None) #ログアウトしたら、session情報を削除する（18行目session['logged_in'] = Trueと比較？）
    flash('ログアウトしました')
    return redirect('/')
    #return redirect(url_for('show_entries'))