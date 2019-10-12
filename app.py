from flask import Flask
from blueprints import api
from flask_cors import CORS
from backend.userddbconn import userddbconn

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'liuytvryuybindsty5ur6t7yu'

app.register_blueprint(api.getapibp())
