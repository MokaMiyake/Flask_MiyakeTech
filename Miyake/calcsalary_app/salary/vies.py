#views:ページの動きを設定する　ページ遷移の指定、計算とか
from flask import request,redirect,url_for,render_template,flash,session
from salary import app

@app.route('/')
def show_salary():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def output():
    print('outputに遷移')
    return render_template('output.html')
