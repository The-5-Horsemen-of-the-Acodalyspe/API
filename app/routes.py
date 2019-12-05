from app import app
from app.schemas import *
from flask import jsonify, request, abort
from flask_jwt import jwt_required


@app.route("/register", methods=["POST"])
def root():
    if not request.json or not all(key in request.json for key in ["username", "password", "email", "firstname", "lastname", "age"]):
        abort(400, "Not enough arguments")

    for i in request.json:

    return jsonify({"Hello": "World"})
