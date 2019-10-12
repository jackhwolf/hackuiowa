from flask import Flask
from blueprints import api

app = Flask(__name__)
app.debug = True

app.register_blueprint(api.getapibp())

app.run()
