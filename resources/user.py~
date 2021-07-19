from ..library import db
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from ..common.models import User


def abort_if_user_doesnt_exist(user_id):
    if not User.query.get(user_id):
        abort(404, message="User with id {} doesn't exist".format(user_id))    

user_parser = reqparse.RequestParser()
user_parser.add_argument(
    'name', dest='name',
    location='form', required=True, 
    help='User\'s name',
)
user_parser.add_argument(
    'address', dest='address',
    location='form', required=True,
    help='User\'s address',
)
user_parser.add_argument(
    'mob_num', dest='mob_num',
    type=int, location='form', 
    required=True, help="User mobile number should be of type int - {error_msg}"
)

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'address': fields.String,
    'mob_num': fields.Integer,
}


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, id=None):
        if not id:
            users = User.query.all()
            return users, 200
        abort_if_user_doesnt_exist(id)      
        return User.query.get(id), 200     
        
    @marshal_with(user_fields)
    def post(self):
        args = user_parser.parse_args(strict=True)
        user = User(name=args.name, address=args.address, mob_num=args.mob_num)
        db.session.add(user)
        db.session.commit()
        return user, 201   
      
    @marshal_with(user_fields)
    def put(self, id):
        args = user_parser.parse_args(strict=True)
        user = User.query.get(id)
        user.name=args.name
        user.address=args.address
        user.mob_num=args.mob_num
        db.session.add(user)
        db.session.commit()
        return user, 201
        
    @marshal_with(user_fields)
    def delete(self, id):
        abort_if_user_doesnt_exist(id)
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return '', 204    
