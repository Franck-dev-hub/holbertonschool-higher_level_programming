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
    usernames = [username for username in users.keys()]
    return (jsonify(usernames))


@app.route("/users/<username>")
def get_user(username):
    """
    get_user - Get user datas
    Return: User data if user exist, else error 404
    """
    if username in users.keys():
        user = users[username]
        return (jsonify(user))
    else:
        error = {"error": "User not found"}
        return (jsonify(error), 404)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add_user - Add user function
    Return: Message 201 if user added, else error 400
    """
    if request.method == "POST":
        content = json.loads(request.data)

        if "username" in content.keys():
            user = {
                "username": content["username"],
                "name": content["name"],
                "age": content["age"],
                "city": content["city"]
            }

            users[user["username"]] = user
            message = "User added"

            return (jsonify({
                "message": message,
                "user": user
            }), 201)

        else:
            message = {"error": "Username is required"}
            return (jsonify(message), 400)


@app.route("/status")
def get_status():
    """
    get_status - Get API status
    Return: OK message if it's ok
    """
    return ("OK")


if __name__ == "__main__":
    app.run()
