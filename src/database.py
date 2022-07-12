from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime
from enum import unique
from sqlalchemy.orm import backref
import string, random

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self):
        return 'User>>> {self.username}'



class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.Column(db.Text, nullable=True)
    icon = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    def gen_short_chars(self):
        characters = string.digits+string.ascii_letters
        picked_chars = ''.join(random.choices(string.ascii_letters,k=3))

        link = self.query.filter_by(short_url=picked_chars).first() 

        if link:
            self.gen_short_chars()

        else:
            return picked_chars

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return "User>>> {self.url}"

