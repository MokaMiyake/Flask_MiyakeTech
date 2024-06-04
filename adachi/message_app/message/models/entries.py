from message import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

# __init__.pyは書かない場合はデフォルトで読み込まれる
    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User id:{} name:{} password:{}>'.format(self.id, self.name, self.password)
    
class Chat(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    user_id1 = db.Column(db.Integer, db.ForeignKey("user.id")) 
    user_id2 = db.Column(db.Integer, db.ForeignKey("user.id")) 
    user = db.relationship("User", back_populates="chats")
    # backrefパラメータはリレーションの逆を定義
    
    room = db.Column(db.String(50))

    def __repr__(self):
        return '<Chat id:{} user_id1:{} user_id2:{} room:{}>'.format(self.id, self.user_id1, self.user_id2, self.room)
    
class Chatmaster(db.Model):
    __tablename__ = 'chatmasters'
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.relationship('Chat', backref='chatmaster', lazy='dynamic')
    to_user = db.relationship('User', backref='chatmaster', lazy='dynamic')
    from_user = db.relationship('User', backref='chatmaster', lazy='dynamic')
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime)


    def __repr__(self):
        return '<Chatmess id:{} chat_id:{} to_user:{} from_user:{} message:{}>'.format(self.id, self.chat_id, self.to_user, self.from_userm, self.message)