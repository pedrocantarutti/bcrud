########################################################
#  $File: routes.py
#  $Date: 14/08/2022
#  $Creator: Pedro Cantarutti
########################################################
import datetime
from flask import jsonify, request, abort
from flask import Blueprint
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from models.user import User


# TODO(pac):
# - Define routes for:
#	* Create user - DONE
#	* Delete user - DONE
#	* Update user (only admins) - 
#	* Retrieve user data - DONE
#	* List all user - DONE

db = SQLAlchemy()
api = Blueprint('api', __name__)


@api.route("/v1", methods=["GET"])
def home():
    return jsonify({"Message": "Basic CRUD API.", "Result": True}), 200


@api.route("/v1/user/list", methods=["GET"])
def get_users():
    users = User.query.all()
    if users:
        return jsonify([repr(user) for user in users]), 200
    return jsonify({"Message": "No users found.", "Result": True}), 404


@api.route("/v1/user/<int:id>", methods=["GET"])
def get_user(id):
    return jsonify(), 200


@api.route("/v1/user", methods=["POST"])
def create_user():
    return jsonify(), 200


@api.route("/v1/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    return jsonify(), 200


@api.route("/v1/user/<int:id>", methods=["PUT"])
def update_user(id):
    return jsonify(), 200


@api.route("/v1/login", methods=["POST"])
def login():
    return jsonify(), 200
