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
from utils import check_if_user_exist


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
    user = User.query.get(id)
    if user:
        return jsonify({"cpf": user.cpf,
                        "password": user.password,
                        "role": user.role,
                        "create_on": user.created_on,
                        "updated_on": user.updated_on}), 200
    return jsonify({"Message": "User not found.", "Result": True}), 404


@api.route("/v1/user", methods=["POST"])
def create_user():
    if not request.json:
        abort(400)
    user = check_if_user_exist(request.json.get("cpf"))
    if user:
        return jsonify({"Message": "User already exists.", "Result": True}), 200
    user = User(
        cpf=request.json.get("cpf"),
        password=request.json.get("password"),
        role=request.json.get("role")
    )
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(repr(user)), 201
    except:
        return jsonify({"Message": "Unable to create user.", "Result": False}), 500


@api.route("/v1/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    return jsonify(), 200


@api.route("/v1/user/<int:id>", methods=["PUT"])
def update_user(id):
    return jsonify(), 200


@api.route("/v1/login", methods=["POST"])
def login():
    return jsonify(), 200
