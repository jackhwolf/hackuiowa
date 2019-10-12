from flask_restplus import Resource, Api, reqparse
from flask import Blueprint
from time import time
from flask_cors import cross_origin
from backend.userddbconn import userddbconn
from backend import backend
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
            parser.add_argument('action')
            parser.add_argument('username', required=True)
            parser.add_argument('password', required=True)
            parser.add_argument('email')
            args = parser.parse_args()
            if args['action'].upper() == 'D':    # delete user
                val = udb.deleteUser(**args)
            elif args['action'].upper() == 'S':  # signup user
                if args.get('email') is None:
                    return {'error': 'email field missing. required for signup'}
                val = udb.signUpUser(**args)
            elif args['action'].upper() == 'L':  # login user
                val = udb.logInUser(**args)
            return val

    @api.route('/weather')
    class weather(Resource):

        def get(self):
            ''' user GETs weather info for themselves '''
            parser.add_argument('latlong', required=False)
            args = parser.parse_args()
            return backend.rainfall()


    return api_bp
