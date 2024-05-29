# viewの処理を記述

from flask import request,redirect,url_for,render_template,flash,session
from salary import app
from salary.calc import calc_salary

@app.route("/")
def show_entries():
    return render_template("input.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    session["input_data"] = ""

    if not request.form["salary"]:
        flash("給与が未入力です。入力してください。")

    elif len(request.form["salary"]) > 10:
        flash("給与には9,999,999,999までが入力可能です。")
        session["input_data"] = request.form["salary"]

    elif request.form["salary"][0] == "-":
        flash("給与にはマイナスの値は入力できません")
        session["input_data"] = request.form["salary"]

    else:
        input_salary = request.form["salary"]

        text_salary = calc_salary(input_salary)
        return render_template("output.html",text_salary=text_salary)
    
    return redirect(url_for("show_entries"))