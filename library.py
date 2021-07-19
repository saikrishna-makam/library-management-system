import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from libraryapi.common.config import config


app = Flask(__name__)
app.config.from_object(config[os.environ.get('API_ENV') or 'default'])
api = Api(app)
db = SQLAlchemy(app)


from libraryapi.resources.user import UserResource
from libraryapi.resources.book import BookResource, UserIssuedBooks
api.add_resource(UserResource, '/users', '/user/<int:id>', endpoint='user')
api.add_resource(BookResource, '/books', '/book/<int:id>', endpoint='book')
api.add_resource(UserIssuedBooks, '/userissued/<int:id>', endpoint='userissued')
