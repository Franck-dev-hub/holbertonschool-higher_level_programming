#!/usr/bin/python3

from flask import Flask, jsonify, request

"""
task_04_flask.py
Set up Flask app
"""

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    content = request.get_json()
    required_fields = {"username", "name", "age", "city"}

    if not content or not required_fields.issubset(content.keys()):
        return jsonify({"error": "Missing field"}), 400

    user = {
            "username": content["username"],
            "name": content["name"],
            "age": content["age"],
            "city": content["city"]
            }

    users[user["username"]] = user
    return jsonify({"message": "User added", "user": user}), 201


@app.route("/status")
def get_status():
    return ("OK")


if __name__ == "__main__":
    app.run(debug=True)
