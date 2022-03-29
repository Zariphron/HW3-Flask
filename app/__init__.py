from flask import Flask

myobj = Flask(__name__)
myobj.config.from_mapping(
        SECRET_KEY = 'this-is-the-secret'
        )

from app import routes
