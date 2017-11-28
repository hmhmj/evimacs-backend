# -*- coding:utf-8 -*-
from flask import Flask

from evimacs import area
from .extensions import api, db, migrate
from evimacs.area.models import Area
from evimacs.price.models import ErShouFangModel

class Config(object):
    DEBUG = True
    DB_NAME = 'lianjia'
    SQLALCHEMY_DATABASE_URI = 'postgresql://evimacs:liu502522@127.0.0.1/{}'.format(DB_NAME)

def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db=db)
    api.init_app(app)
    # init_app(app)
    register_shellcontext(app)
    return app

def register_shellcontext(app):
    def shell_context():
        return {
            'db': db
            }
    app.shell_context_processor(shell_context)

def init_app(app):
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
