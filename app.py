from flask import Flask, render_template
from blueprints import api
from flask_cors import CORS
from backend.userddbconn import userddbconn

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SECRET_KEY'] = 'liuytvryuybindsty5ur6t7yu'

app.register_blueprint(api.getapibp())

@app.route('/landing')
def landing():
    return render_template('floods/public/index.html')
