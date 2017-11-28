# -*- coding:utf-8 -*-

import types

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()
csrf_protect = CsrfProtect()
api=Api(decorators=[csrf_protect.exempt])

def api_route(self, *args, **kwargs):
    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper

api.route = types.MethodType(api_route, api)
