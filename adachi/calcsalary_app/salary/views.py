from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

# 最初のページ
@app.route("/")
def show_salary():
    return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def input():
    income = 0
    tax = 0
    if request.method == 'POST': # 正しく送信
        suuzi = int(request.form['money'])
        tax = calc(suuzi)
        income = suuzi - tax
        # flash('計算結果を出力')
        # return redirect(url_for('show_salary'))
    return render_template('output.html',suuzi=suuzi,income=income,tax=tax)



# 税金の計算
def calc(suuzi):
    tax = 0 #　税
    income = 0 #　手取り

    if suuzi >= 1000000:
        tax = int((suuzi-1000000) * 0.2) + int(1000000 * 0.1)
    else:
        tax = int(suuzi * 0.1)

    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    income = suuzi - tax

    # ターミナル上での確認用
    print("支給額:"+str(income)+"、税額:"+str(tax),end="")

    return tax