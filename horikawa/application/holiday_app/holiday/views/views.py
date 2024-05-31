from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from decimal import Decimal, ROUND_HALF_UP
from holiday.models.mst_holiday import Holiday
from holiday import db
from .input import insert_update,delete

# 最初のページ
@app.route("/")
def show_input():
    return render_template('input.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if not request.form["holi_date"]:
        flash("日付が入力されていません")
    else:
        # 新規登録・更新
        if request.form["button"] == "insert_update":
            if not request.form["holi_text"]:
                flash("テキストが入力されていません")
            elif len(request.form["holi_text"]) > 20:
                flash("テキストの文字数上限を超えています(20文字)")
            else:
                date = request.form["holi_date"]
                text = request.form["holi_text"]
                
                insert_update(date,text)

        # 削除
        elif request.form["button"] == "delete":
            date = request.form["holi_date"]
            delete(date)
            
    return redirect(url_for("show_input"))

# 一覧表示
@app.route('/list', methods=['GET'])
def list_view():
    entries = Holiday.query.order_by(Holiday.holi_date).all()
    return render_template("list.html",entries=entries)