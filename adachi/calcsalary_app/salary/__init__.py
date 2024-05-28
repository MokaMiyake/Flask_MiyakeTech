from flask import Flask

app = Flask(__name__)

import salary.views

app.config.from_object("salary.config")



