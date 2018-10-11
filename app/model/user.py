#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.plugins import db
from app.plugins import ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User ID: {self.id}>'


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    books = ma.List(ma.HyperlinkRelated('book_detail'))


user_schema = UserSchema()
users_schema = UserSchema(many=True)
