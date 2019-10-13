from flask_restplus import Resource, Api, reqparse
from flask import Blueprint
from time import time
from flask_cors import cross_origin
import requests
import os
import json
from dotenv import load_dotenv
from backend.userddbconn import userddbconn


load_dotenv()

# create and return out API to tie to our app in hackuiowa/app.py
def getapibp():

    # setup Flask objects
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp,
              default="hackuiowa-project-api",
              default_label="hackuiowa-project-api docs")

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

    # how user requests rainfall info
    @api.route('/checkrainfall')
    class checkrainfall(Resource):

        def get(self):
            ''' user GETs weather info for themselves '''
            print(1)
            url = f"https://api.darksky.net/forecast/{os.environ.get('weatherKey')}/43.0731,89.4012"
            print(2)
            r = requests.get(url)
            r = r.json()
            daily = r['daily']['data']
            print(json.dumps(daily, indent=4))
            daily = list(map(lambda x: [x['time'], x['precipIntensityMax']*24], daily))
            return daily

    return api_bp
