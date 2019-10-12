from flask import Flask
from blueprints import api
from flask_cors import CORS
from backend.userddbconn import userddbconn

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "http://localhost:port"}})

app.config['SECRET_KEY'] = 'liuytvryuybindsty5ur6t7yu'
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(api.getapibp())
