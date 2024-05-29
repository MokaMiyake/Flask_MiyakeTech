from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_salary():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def output():
    input_sarary = int(request.form['salary'])
    allowance = 0
    input_salary = 0
    tax = 0
    if request.method=='POST':
        if input_sarary >= 1000000:
            #flash('')
            tax1 = (input_salary - 1000000) * 0.2
            tax2 = 1000000 * 0.1
            tax = tax1 + tax2
        #elif == "":
            #flash('給与が未入力です。入力してください。')
        elif len(input_salary) >= 11:
            flash('給与には最大9,999,999,999まで入力可能です。')
        elif input_salary < 0:
            flash('給与にはマイナスの値は入力できません。')
        else:
            tax = input_salary * 0.1

        tax =Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        allowance = input_salary - tax
        print("支給額:"+ str(allowance)+"、税額:"+ str(tax),end="")

    return render_template('output.html',input_salary=input_sarary,allowance=allowance,tax=tax)
