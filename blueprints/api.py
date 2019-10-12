from flask_restplus import Resource, Api, reqparse
from flask import Blueprint
from time import time
from backend.userddbconn import userddbconn

# create and return out API to tie to our app in hackuiowa/app.py
def getapibp():

    # setup Flask objects
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp,
              default="hackuiowa-project-api",
              default_label="hackuiowa-project-api docs",
              url_prefix='/api',
              doc='/api/apidoc/')

    # define stuff for users
    @api.route('/user')
    class user(Resource):
        ''' all things user -- login, signup, logout(?) '''

        def get(self):
            ''' see if a user exists '''
            parser = reqparse.RequestParser()
            parser.add_argument('username', required=True)
            parser.add_argument('password', required=True)
            args = parser.parse_args()
            if args['username'] and args['password']:
                print(f"\n{int(time())}: User.get({args['username']}, {args['password']}) -- > 1\n")
                return {'Response': 1}
            print(f"\n{int(time())}: User.get({args['username']}, {args['password']}) -- > 0\n")
            return {'Response': 0}

        def post(self):
            ''' add new user '''
            parser = reqparse.RequestParser()
            parser.add_argument('username', required=True)
            parser.add_argument('password', required=True)
            args = parser.parse_args()
            print(f"{int(time())}: User.get({args['username']}, {args['password']}) -- > 1")
            return {'Response': 1}

    return api_bp
