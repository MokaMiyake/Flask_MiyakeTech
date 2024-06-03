from flask import request,redirect,url_for,render_template,flash,session
from myMail import app
# from mail.models.entries import MailList メールリストデータベース
from myMail import db
from myMail.models.entries import MailList
from .views import login_required
from .mail_control import sent_mail



@app.route("/")
@login_required
def show_entries():
    # "@login_required"で下記2行のコードをviews/views.py内のlogin_required関数で実行
    # if not session.get("logged_in"):
    #     return redirect(url_for("login"))
    
    print("session.get('logged_in'):" + str(session.get("logged_in")))

    entries = MailList.query.filter(MailList.address == app.config["LOGINACCOUNT"]).all()
    return render_template("entries/list.html",entries=entries)
    
    # return render_template("entries/list.html")

@app.route("/entries/<int:id>", methods=["GET"])
@login_required
def show_entry(id):
    entry = MailList.query.get(id)
    return render_template("entries/show.html", entry=entry)

@app.route("/sent_mail", methods=['GET', 'POST'])
@login_required
def sent_mail():
    print("メール送信が実行されました")
    print("ログインしているaccountは" + app.config["LOGINACCOUNT"])
    
    bool_address = True
    bool_title = True
    bool_text = True
    
    if not request.form["address"]:
        bool_address = False
    if not request.form["title"]:
        bool_title = False
    if not request.form["text"]:
        bool_text = False
    
    
    #####################################
    # バリデーション

    getAddress = False
    for account in app.config["ACCOUNT"]:
        if request.form["address"] == account[0]:
            getAddress = True

    #####################################
    

    if not bool_address or not bool_title or not bool_text:
        flash("宛先" + str(bool_address) + ",件名" + str(bool_title) + ",本文" + str(bool_text))
    elif not getAddress:
        flash("宛先のユーザーが存在しません")
    else:
        flash("メールが送信されました")

        # 7行目のfromの表記がバグの原因っぽい気がする
        # sent_mail(request.form["address"],app.config["LOGINACCOUNT"],request.form["title"],request.form["text"])


    return redirect(url_for("show_entries"))