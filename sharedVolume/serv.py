from flask import Flask, render_template
import connexion, os
import conf
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from waitress import serve



basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = conf.connex_app
connex_app.add_api('swagger.yml')



@connex_app.route('/')
def home():
    return render_template('home.html')




if __name__ == '__main__':
    # connex_app.run(host='0.0.0.0', port=5000, debug=True)
    serve(connex_app, host="0.0.0.0", port=5000)