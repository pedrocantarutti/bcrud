########################################################
#  $File: user.py
#  $Date: 14/08/2022
#  $Creator: Pedro Cantarutti
########################################################
import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """ User model for users db table """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(8), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_on = db.Column(db.DateTime, default=datetime.datetime.now())
    role = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, cpf, password, role=False):
        self.cpf = cpf
        self.password = password # use bcrypt later on to generate password hash
        self.role = role

    def __repr__(self):
        return f'User {self.cpf} create on {self.created_on}'

    @property
    def serialize(self):
        return {
            'cpf': self.cpf,
            'password': self.password,
            'role': self.role,
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }
