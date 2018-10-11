#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

from app.api import create_blueprint_v1
from app.plugins import db, migrate, api, ma
from app.shell import UserCommand


def load_configs(app):
    app.config.from_object('app.config.settings')
    app.config.from_object('app.config.confidential')


def register_blueprints(app):
    app.register_blueprint(create_blueprint_v1())


def add_commands(app):
    app.cli.add_command(UserCommand)


def attach_plugins(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    ma.init_app(app)


def create_app():
    app = Flask(__name__)

    load_configs(app)
    attach_plugins(app)
    register_blueprints(app)
    add_commands(UserCommand)

    return app
