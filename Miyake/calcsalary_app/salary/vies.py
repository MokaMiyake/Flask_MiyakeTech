#給与計算アプリ
#views:ページの動きを設定する　ページ遷移の指定、計算とか
from flask import request,redirect,url_for,render_template,flash,session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_salary():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def output():
    print('outputに遷移')
    salary = int(request.form['salary'])

#税額の計算
    if salary > 1000000:
        tax = (salary-1000000) * 0.2 + 100000
    elif salary <= 1000000:
        tax = salary * 0.1
#四捨五入の計算
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
#支給額の計算
    pay_amount = salary - tax
    return render_template('output.html', salary=salary, pay_amount=pay_amount, tax=tax)


@app.route('/input', methods=['GET'])
def input():
    return render_template('input.html')


