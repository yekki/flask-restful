#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Blueprint

__all__ = ['create_blueprint_v1']


def create_blueprint_v1():
    from app.api.v1 import book, user
    bp_v1 = Blueprint('v1', __name__, url_prefix='/v1')

    user.api.register(bp_v1, url_prefix='/user')
    book.api.register(bp_v1, url_prefix='/book')

    return bp_v1
