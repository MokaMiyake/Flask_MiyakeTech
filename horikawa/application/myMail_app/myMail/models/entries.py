from myMail import db
from datetime import datetime

# メールリストDB
class MailList(db.Model):
    __tablename__="mail_list"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(30))
    from_address = db.Column(db.String(30))
    title = db.Column(db.String(30))
    text = db.Column(db.Text)
    sent_at = db.Column(db.DateTime)

    def __init__(self, address=None, from_address=None, title=None, text=None):
        self.address = address
        self.from_address = from_address
        self.title = title
        self.text = text
        self.sent_at = datetime.utcnow()

    def __repr__(self):
        return "<MailList id:{} address:{} from_address:{} title:{} text:{}>".format(self.id, self.address, self.from_address, self.title, self.text)
    


# 一般ユーザーアカウントDB
