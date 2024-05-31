# Flask appの初期化を行い、Flask appオブジェクトの実態を持つ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("holiday.config")

db = SQLAlchemy(app)

from holiday.views import views




