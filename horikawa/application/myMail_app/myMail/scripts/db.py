from flask_script import Command
from myMail import db
from myMail.models.entries import MailList

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()