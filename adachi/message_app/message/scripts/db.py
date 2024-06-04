
from flask_script import Command
from message import db
from message.models.entries import User, Chat, Chatmess


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()