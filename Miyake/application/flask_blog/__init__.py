from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_blog.config') #flask_blogフォルダ内のconfig.pyの内容をconfigとして扱う

db = SQLAlchemy(app)

# import Miyake.application.flask_blog.views.views
from flask_blog.views import views, entries
