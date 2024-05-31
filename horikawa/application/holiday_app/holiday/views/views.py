from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from decimal import Decimal, ROUND_HALF_UP
from holiday.models.mst_holiday import Holiday
from holiday import db

# 最初のページ
@app.route("/")
def show_input():
    return render_template('input.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.form["button"] == "insert_update":
        flash("新規登録・更新が実行されました")
    elif request.form["button"] == "delete":
        flash("削除が実行されました")
    return redirect(url_for("show_input"))

# 一覧表示
@app.route('/list', methods=['POST'])
def list_view():
    entries = Holiday.query.order_by(Holiday.holi_date).all()
    return render_template("list.html",entries=entries)