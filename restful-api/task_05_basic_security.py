#!/usr/bin/python3
"""
Module Name: task_05_basic_security.

Contains functions to manage user authentication.
"""
from flask import Flask, request, jsonify
from markupsafe import escape
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import get_jwt_identity

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Unrequired Homepage </h1> " \
           "<p> Pages available: " \
           "<br>'/basic-protected', </br>" \
           "'/login'.</p>"

auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "user2": {"username": "user2",
              "password": generate_password_hash("password2"),
              "role": "regular_user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username not in users:
        return None
    hash_password = users[username].get("password")
    if not hash_password:
        return None
    if check_password_hash(hash_password, password):
        return username

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_auth():
        return "Basic Auth: Access Granted", 200

app.config["JWT_SECRET_KEY"] = "supposedly_secret-key"
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not verify_password(username, password):
        return "no token for you", 401
    access_token = create_access_token(identity=users[username])
    return jsonify({"access_token": access_token}), 200
    
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def JWT_auth():
    return "JWT Auth: Access Granted", 200

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def JWT_role_auth():
    user = get_jwt_identity()
    if user.get("role") == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(token_header, token_payload):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(token_header, token_payload):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(token_header, token_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(token_header, token_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(token_header, token_payload):
    return jsonify({"error": "Fresh token required"}), 401

@jwt.user_lookup_error_loader
def handle_user_lookup_error(token_header, token_payload):
    return jsonify({"error": "Token has been revoked"}), 401

if __name__ == "__main__":
    app.run()
