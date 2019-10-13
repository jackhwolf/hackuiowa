from flask_restplus import Resource, Api, reqparse
from flask import Blueprint
from time import time
from flask_cors import cross_origin
import requests
import json
from backend.userddbconn import userddbconn
from backend import logic


# create and return out API to tie to our app in hackuiowa/app.py
def getapibp():


    # setup Flask objects
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp,
              default="hackuiowa-project-api",
              default_label="hackuiowa-project-api docs")

    log = logic.logic()


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

    # for the user to get rain/flood info
    @api.route('/floodwatch')
    class floodwatch(Resource):

        def post(self):
            ''' user GETs weather info for themselves '''
            parser = reqparse.RequestParser()
            parser.add_argument('address', required=True)  # , required=True)
            args = parser.parse_args()
            rainfall = log.checkrainfall(args['address'])
            danger   = log.relativedanger(args['address'])
            summary = log.summarize(rainfall, danger)
            return {'rainfall': rainfall,
                    'danger': danger,
                    'summary': summary}


    return api_bp
