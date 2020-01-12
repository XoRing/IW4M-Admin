"""
The flask application package.
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from master.context.base import Base
from os import environ

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = environ.get('IW4MADMIN_JWT_SECRET')
app.config['JWT_IDENTITY_CLAIM'] = 'sub'
app.config['PROPAGATE_EXCEPTIONS'] = True
jwt = JWTManager(app)
api = Api(app)
ctx = Base()

from .util import filters
import master.routes
import master.views
