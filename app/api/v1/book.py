#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.libs import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'this is a book'


@api.route('/create')
def create_book():
    return 'create book'
