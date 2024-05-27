from flask import Flask

app = Flask(__name__)

import flask_blog.views

app.config.from_object('flask_blog.config') #flask_blogフォルダ内のconfig.pyの内容をconfigとして扱う

