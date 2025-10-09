#!/usr/bin/python3

from flask import Flask, jsonify, request
import json

"""
task_04_flask.py
Set up Flask app
"""

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    home - Welcome to the api function
    Return: Welcome message
    """
    return ("Welcome to the Flask API!")


@app.route("/data")
def get_usernames():
    """
    get_usernames - Get usernames
    Return: list of users
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    get_user - Get user datas
    Return: User data if user exist, else error 404
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add_user - Add user function
    Return: Message 201 if user added, else error 400
    """
    content = json.loads(request.data)

    if "username" in content.keys():
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
    """
    get_status - Get API status
    Return: OK message if it's ok
    """
    return ("OK")


if __name__ == "__main__":
    app.run()
