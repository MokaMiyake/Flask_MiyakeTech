from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

# 最初のページ
@app.route("/")
def show_holiday():
    return render_template('input.html')

@app.route('/result', methods=['GET', 'POST'])
def holiday():
    holidate=request.form['holi_date']
    holitext=request.form['holi_text']
    status = 0
    if request.form['button']=="insert-update":
        # 登録
        if Holiday.query.get(holidate) == None:
            holiday = Holiday(
                holi_date=holidate,
                holi_text=holitext
            )
            db.session.add(holiday)
            print(Holiday.query.get(holidate))
        # 更新
        else:
            holiday = Holiday.query.get(holidate)
            holiday.holi_text = holitext
            status = 1

        db.session.commit()
    
    # 削除
    elif request.form['button']=="dalete":
        print( Holiday.query.get(holidate))
        if Holiday.query.get(holidate) != None:
            holiday = Holiday.query.get(holidate)
            db.session.delete(holiday)
            db.session.commit()
            status = 2
        else:
            flash('{{ holiday }}は祝日マスタに登録されていません。')
            return redirect(url_for('show_holiday'))
    
    return render_template("result.html",holi_date=holidate,holi_text=holitext,status=status)


@app.route('/list', methods=['GET', 'POST'])
def view_holiday():
    holiday = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template("list.html",holiday=holiday)
