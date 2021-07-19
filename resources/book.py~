from datetime import datetime
from ..library import db
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from ..common.models import Book, User
from .user import abort_if_user_doesnt_exist


def abort_if_book_doesnt_exist(book_id):
    if not Book.query.filter_by(id=book_id).first():
        abort(404, message="Book with id {} doesn't exist".format(book_id)) 

book_parser = reqparse.RequestParser()
book_parser.add_argument(
    'title', dest='title',
    location='form', required=True,
    help='Book\'s title',
)
book_parser.add_argument(
    'author', dest='author',
    location='form', required=True,
    help='Book\'s author',
)
book_parser.add_argument(
    'publication', dest='publication',
    location='form', required=True,
    help='Book\'s publication',
)
book_parser.add_argument(
    'user_id', dest='user_id',
    type=int, location='form', 
    required=True, help='User id should be of type int - {error_msg}',
)

book_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'author': fields.String,
    'publication': fields.String,
    'issued_on': fields.DateTime,
    'user_id': fields.Integer,
}


class BookResource(Resource):
    @marshal_with(book_fields)
    def get(self, id=None):
        if not id:
            books = Book.query.all()
            return books, 200
        abort_if_book_doesnt_exist(id)
        return Book.query.get(id), 200
        
    @marshal_with(book_fields)
    def post(self):
        args = book_parser.parse_args(strict=True)
        abort_if_user_doesnt_exist(args.user_id)
        book = Book(title=args.title, author=args.author, publication=args.publication, issued_on=datetime.utcnow(), user_id=args.user_id)
        db.session.add(book)
        db.session.commit()
        return book, 201
    
    @marshal_with(book_fields)
    def put(self, id):
        args = book_parser.parse_args(strict=True)
        abort_if_user_doesnt_exist(args.user_id)
        book = Book.query.get(id)
        book.title = args.title
        book.author= args.author
        book.publication = args.publication
        book.user_id = args.user_id
        db.session.add(book)
        db.session.commit()
        return book, 201
    
    @marshal_with(book_fields)
    def delete(self, id): 
        abort_if_book_doesnt_exist(id)
        Book.query.filter_by(id=id).delete()
        db.session.commit()
        return '', 204
        
        
class UserIssuedBooks(Resource):
    @marshal_with(book_fields)
    def get(self, id):
        abort_if_user_doesnt_exist(id)
        return User.query.get(id).books.all(), 200    
