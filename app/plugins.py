#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
api = Api()
ma = Marshmallow()
