#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.plugins import db, ma
from app.model.user import UserSchema


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    designer_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    designer = db.relationship('User', backref='products')

    def __repr__(self):
        return f'<Product ID: {self.id}>'


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product

    designer = ma.Nested(UserSchema)

    links = ma.Hyperlinks({
        'self': ma.URLFor('product_detail', id='<id>'),
        'collection': ma.URLFor('product_list')
    })
