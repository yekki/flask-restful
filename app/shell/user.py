#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import random
import string
from flask.cli import AppGroup

from app.libs import echo
from app.model import Product
from app.model import User
from app.plugins import db

user_cli = AppGroup('user')


@user_cli.command('add')
@click.argument('username')
@click.argument('password')
def create_user(username, password):
    user = User.query.filter(User.username == username).first()

    if user:
        echo(f'User:{username} is already exist, please change another one.', fg='red')
    else:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        echo(f'User:{username} created.', fg='green')


@user_cli.command('del')
@click.argument('username')
def delete_user(username):
    user = User.query.filter(User.username == username).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        echo(f'User:{username} created.', fg='green')
    else:
        echo(f'User:{username} not exist at all.', fg='red')


@user_cli.command('list')
def list_user():
    users = User.query.all()
    for user in users:
        echo(f'{user}', fg='green')


@user_cli.command('cleanup')
def list_user():
    db.drop_all()
    db.create_all()
    echo(f'Database is cleaned.', fg='green')


@user_cli.command('samples')
def gen_sample_data():
    for i in range(10):
        user = User(username=f'user{i}', password='password')

        for j in range(10):
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            Product(name=name, designer=user)

        db.session.add(user)
        db.session.commit()
        echo(f'{user} added.', fg='blue')
    echo('sample data generated.', fg='green')
