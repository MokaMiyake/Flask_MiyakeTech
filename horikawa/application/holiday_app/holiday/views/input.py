# 入力操作 Python
from flask import flash
from holiday.models.mst_holiday import Holiday
from holiday import db

# SQLデータの新規登録
def insert_update(date, text):
    print(date + "と" + text + "を受け取った")
    print("存在するかどうか" + str(checkDate(date)))

    # holiday_dateが既に存在するかを確認する処理
    if not checkDate(date):
        holiday = Holiday(
            holi_date = date,
            holi_text = text
        )

        flash(date + f"({text})が登録されました")
    else:
        holiday = Holiday.query.get(date)
        print(holiday)
        holiday.holi_date = date
        holiday.holi_text = text

        flash(date + f"は({text})に更新されました")

    db.session.merge(holiday)
    db.session.commit()

# SQLデータの削除
def delete(date):
    if not checkDate(date):
        flash("祝日マスタが登録されていません")
        pass
    
    holiday = Holiday.query.get(date)
    text = holiday.holi_text

    db.session.delete(holiday)
    db.session.commit()
    flash(date + f"({text})は削除されました")


def checkDate(date):
    return Holiday.query.get(date) != None