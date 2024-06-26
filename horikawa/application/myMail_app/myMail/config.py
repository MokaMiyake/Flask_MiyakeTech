import os
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
    "user": os.getenv("DB_USER","root"),
    "password": os.getenv("DB_PASSWORD", "mysql"),
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_DATABASE", "ENSHU")
})
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
SECRET_KEY = "secret key"

# 管理者アカウント
USERNAME = "john"
PASSWORD = "due123"

# 一般ユーザーアカウント
ACCOUNT = [["horikawa@mymail.com","myna123"],["adachi@mymail.com","sql123"],["fujii@mymail.com","flask123"]]


LOGINACCOUNT = "adachi@mymail.com"