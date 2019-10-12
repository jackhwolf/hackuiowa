from flask import Flask
from blueprints import api
from backend.userddbconn import userddbconn

app = Flask(__name__)
app.register_blueprint(api.getapibp())
