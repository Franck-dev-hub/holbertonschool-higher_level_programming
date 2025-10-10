#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity,
                                jwt_required,
                                JWTManager
                                )

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '827ff949acc149358890154ce1b870fe'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
  "admin1": {
    "username": "admin1",
    "password": generate_password_hash("password"),
    "role": "admin"
    },
  "user1": {
    "username": "user1",
    "password": generate_password_hash("password"),
    "role": "user"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/')
def index():
    return "Welcome to the Flask API!"


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def check_basic_login():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def post_simple_login():
    payload = request.get_json()
    username = payload.get('username', None)
    password = payload.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    authed_user = verify_password(username, password)
    if authed_user is not None:
        new_token = create_access_token(identity=authed_user)
        return jsonify(access_token=new_token)

    else:
        return jsonify({"message": "Bad username of password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected_login():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only_login():
    current_user = get_jwt_identity()

    if current_user not in users:
        return jsonify({"error": "User not found"}), 404

    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
