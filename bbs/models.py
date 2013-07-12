import datetime
from bbs import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.Unicode(20), nullable=False)
    title = db.Column(db.Unicode(100), nullable=False)
    body = db.Column(db.UnicodeText, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    views = db.Column(db.Integer, nullable=False, default=0)
