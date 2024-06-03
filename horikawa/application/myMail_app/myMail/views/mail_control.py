# メールリスト操作 Python
from flask import flash
from myMail.models.entries import MailList
from myMail import db

# メール送信
def sent_mail(getAddress, getFrom_address, getTitel, getText):
    pass
    # mailList = MailList(
    #     address = getAddress,
    #     from_address = getFrom_address,
    #     title = getTitel,
    #     text = getText
    # )

    flash("メールが送信されました")
    # db.session.merge(mailList)
    # db.session.commit()