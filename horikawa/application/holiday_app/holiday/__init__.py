# Flask appの初期化を行い、Flask appオブジェクトの実態を持つ

from flask import Flask

app = Flask(__name__)

import holiday.views.views

app.config.from_object("holiday.config")



