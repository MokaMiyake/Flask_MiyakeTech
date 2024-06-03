from flask import request,redirect,url_for,render_template,flash,session
from myMail import app
from functools import wraps

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))

        return view(*args, **kwargs)
    
    return inner

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":

        if not request.form["username"]:
            flash("アカウント名が入力されていません")
        elif not request.form["password"]:
            flash("パスワードが入力されていません")
        else:
            username = request.form["username"]
            password = request.form["password"]
            # 管理者アカウントへのログイン
            if username == app.config["USERNAME"] and password == app.config["PASSWORD"]:
                flash("管理者アカウントでログインしました")
                session["logged_in"] = True
                return redirect(url_for("show_entries"))

            #####################################
            # 一般ユーザーアカウントへのログイン
            else:
                for account in app.config["ACCOUNT"]:
                    if username == account[0] and password==account[1]:
                        flash("ログインしました")

                        # ログインアカウント名を変数に格納
                        app.config["LOGINACCOUNT"] = username
                        session["logged_in"] = True
                        return redirect(url_for("show_entries"))

            #####################################
        flash("アカウント名・またはパスワードが違います")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in",None)
    flash("ログアウトしました")
    return redirect(url_for("show_entries"))