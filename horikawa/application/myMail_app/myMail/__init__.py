from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("myMail.config")

db = SQLAlchemy(app)

from myMail.views import views,entries