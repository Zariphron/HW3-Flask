from flask import Flask

myapp_obj = Flask(__name__)
myapp_obj.config.from_mapping(
        SECRET_KEY = 'this-is-the-secret'
        )

from app import routes
