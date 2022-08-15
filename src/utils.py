########################################################
#  $File: utils.py
#  $Date: 13/08/2022
#  $Creator: Pedro Cantarutti
########################################################
import config
from functools import wraps
from models.user import User
from sqlalchemy.orm.exc import NoResultFound
from flask import request, jsonify
import jwt
import datetime


def check_if_user_exist(cpf):
    try:
        user = User.query.filter(User.cpf == cpf).one()
        if user:
            return user
    except NoResultFound:
        return None


def generate_token(cpf):
    """ Generates JWT token and sets expiration date to 10 min """
    expiration_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)
    jtoken = jwt.encode(
        {
            "cpf": cpf,
            "exp": expiration_date},
            config.SECRET_KEY
    )
    return jtoken, expiration_date


def can_access(func):
    """ Decorator that will be use to check if user can access a given endpoint """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"Message": "Token is missing", "Result": False}), 401
        try:
            decoded_data = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
            d = datetime.datetime.fromtimestamp(decoded_data["exp"])
            user = check_if_user_exist(decoded_data["cpf"])
        except jwt.ExpiredSignatureError:
            return jsonify({"Message": "Token expired, you need log in again.", "Result": False}), 403
        except jwt.InvalidTokenError:
            return jsonify({"Message": "Invalid token. Please log in again.","Result": False}), 403
        return func(user, *args, **kwargs)
    return wrapper
