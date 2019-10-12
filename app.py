from flask import Flask
from blueprints import api
from backend.userddbconn import userddbconn

app = Flask(__name__)
app.debug = True

app.register_blueprint(api.getapibp())

app.run()
