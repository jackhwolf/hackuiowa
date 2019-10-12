from flask_restplus import Resource, Api, reqparse
from flask import Blueprint
from time import time
from flask_cors import cross_origin
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
    @cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
    class user(Resource):
        ''' all things user -- login, signup, logout(?) '''

        def get(self):
            ''' see if a user exists '''
            udb = userddbconn()
            parser = reqparse.RequestParser()
            parser.add_argument('username', required=True)
            parser.add_argument('password', required=True)
            args = parser.parse_args()
                return udb.doesUserExist(**args)

        def post(self):
            ''' add/delete new user '''
            udb = userddbconn()
            parser = reqparse.RequestParser()
            parser.add_argument('username', required=True)
            parser.add_argument('password', required=True)
            parser.add_argument('email')
            parser.add_argument('delete', type=int, default='0')
            args = parser.parse_args()
            if args['delete'] == 1:
                val = udb.deleteUser(**args)
            else:
                if args.get('email') is None:
                    return {'error': 'EMAIL field missing. required for signup'}
                val = udb.signUpUser(**args)
            return val

    return api_bp
