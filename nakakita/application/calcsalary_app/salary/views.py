from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/')
def show_salary():
    return render_template('input.html')

@app.route('/output',methods=['GET','POST'])
def input():
    if request.method=='POST':
        input_sarary = request.form['salary']
        if input_sarary > 1000000:
            #flash('')
            input_salary = 0
            tax = 0
            tax1 = (input_salary - 1000000) * 0.2
            tax2 = 1000000 * 0.1
            tax = tax1 + tax2
        else:
            tax = input_salary * 0.1
            #return redirect(url_for('show_entries'))

        allowance = 0
        tax =Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
        allowance = input_salary - tax
    return render_template('input.html')
