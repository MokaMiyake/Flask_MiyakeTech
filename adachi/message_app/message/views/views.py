from flask import request, redirect, url_for, render_template, flash, session
from message import app
from message import db
from message.models.entries import User
from functools import wraps


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('user_id'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': # 正しく送信
        name = request.form.get("name")
        password = request.form.get("password")
        user = User.query.filter_by(name=name).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect("/userlist")
    else:
        return redirect(url_for('login_get'))



@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('ログアウトしました')
    return redirect(url_for('login_get'))

# アカウント作成(新規ユーザー登録)プログラム
@app.route("/regist", methods=["POST"])
def regist():
    user = User(
        name=request.form['name'],
        password=request.form['password']
    )
    db.session.add(user)
    db.session.commit()
    flash('新しくアカウントを作成しました')
    
    session['user_id'] = user.id
    return redirect("/userlist")

@app.route("/userlist")
def userlist():
    users = User.query.all()
    return render_template("userlist.html", tpl_user_info=users)