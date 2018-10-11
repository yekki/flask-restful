#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify
from app.libs import Redprint
from app.model.user import User, users_schema, user_schema

api = Redprint('book')

@api.route('/')
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)
    # OR
    # return user_schema.jsonify(all_users)


@api.route('/<id>')
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)
