########################################################
#  $File: app.py
#  $Date: 14/08/2022
#  $Creator: Pedro Cantarutti
########################################################
from flask import Flask
from routes.routes import api
from models.user import db


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
app.register_blueprint(api)


if __name__=='__main__':
    app.debug = True
    app.run()
