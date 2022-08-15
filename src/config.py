########################################################
#  $File: config.py
#  $Date: 14/08/2022
#  $Creator: Pedro Cantarutti
########################################################
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(32)
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'crud.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
