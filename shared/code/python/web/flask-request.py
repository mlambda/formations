from flask import request

def login():
    if "username" in request.form:
        username = request.form["username"]
        password = request.form["password"]