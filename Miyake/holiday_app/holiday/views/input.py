from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def add_holiday():
    if request.form["button"] == "insert_update":
        #IF入力日がデータベースにない場合、新規登録し「登録されました」elifある場合、更新し「更新されました」
        #(データベースに入れる処理する)
        holi_date = request.form['holiday']
        holi_text = request.form['holiday_text']
        return render_template('result.html',holi_date=holi_date, holi_text=holi_text)

    elif request.form["button"] == "delete":
        #データを削除する処理
        holi_date = request.form['holiday']
        holi_text = request.form['holiday_text']
        return render_template('result.html',holi_date=holi_date, holi_text=holi_text)
    
@app.route('/list', methods=['GET'])
def show_list():
    holiday = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template('list.html', holiday=holiday)

