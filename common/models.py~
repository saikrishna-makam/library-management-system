from  ..library import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.Text())
    mob_num = db.Column(db.Integer)
    books = db.relationship('Book', backref='user', lazy='dynamic')
    

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    publication = db.Column(db.String(64))
    issued_on = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.ForeignKey('users.id'))    
