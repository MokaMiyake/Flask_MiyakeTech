from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("message.config")

db = SQLAlchemy(app)

from message.views import chat


