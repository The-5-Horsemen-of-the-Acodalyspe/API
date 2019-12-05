from app import app
from app.schemas import *
from flask import jsonify
from flask_jwt import jwt_required


@app.route("/", methods=["GET"])
@jwt_required()
def root():
    return jsonify({"Hello": "World"})
