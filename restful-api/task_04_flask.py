#!/usr/bin/python3
"""
Module Name: task_04_flask.

Contains a flask server.
"""
from flask import Flask
from flask import jsonify
from markupsafe import escape
from flask import request

app = Flask(__name__)
users = {}
@app.route("/")
def home():
    return "Welcome to the Flask API!"
@app.route("/data")
def list_usernames():
    return jsonify(list(users.keys()))
@app.route("/users")
def list_users():
    return jsonify(list(users.keys()))
@app.route("/status")
def status():
    return "OK"
@app.route("/users/<username>")
def user_data(username):
    if escape(username) not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[escape(username)]), 200
@app.route("/add_user", methods=["POST"])
def add_user():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    # if username in users:
    #     return jsonify({"error": "Username already exists"}), 409
    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    name = data["name"]
    if "age" not in data:
        return jsonify({"error": "Age is required"}), 400
    age = data["age"]
    if "city" not in data:
        return jsonify({"error": "City is required"}), 400
    city = data["city"]
    # name = data.get("name", "NoName")
    # age = data.get("age", 0)
    # city = data.get("city", "NoCity")

    users[username] = {"username": username,
                       "name": name,
                       "age": age,
                       "city": city}
    return jsonify({"message": "User added",
                    "user": users[username]}), 201

    

if __name__ == "__main__":
    app.run()
