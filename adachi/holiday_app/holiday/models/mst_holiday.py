from holiday_app import db
from datetime import datetime

class Holiday(db.Model):

    def __init__(self, holi_date=None, holi_text=None):
        self.holi_date = holi_date
        self.holi_text = holi_text

    def __repr__(self):
        return '<Holiday holi_date:{} holi_text:{}>'.format(self.holi_date, self.holi_text)