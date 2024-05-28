# viewの処理を記述

from flask import request,redirect,url_for,render_template,flash,session
from salary import app
from salary.calc import calc_salary

@app.route("/")
def show_entries():
    return render_template("input.html")

@app.route("/calc", methods=["GET", "POST"])
def calc():
    # if request.method == "POST":
    print("計算実行")

    if not request.form["salary"]:
        print("数値を入力してください")
    else:
        input_salary = request.form["salary"]

        text_salary = calc_salary(input_salary)
        return render_template("output.html",text_salary=text_salary)
    return redirect(url_for("show_entries"))