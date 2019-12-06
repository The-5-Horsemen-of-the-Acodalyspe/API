from app import app
from app.schemas import *
from flask import jsonify, request, abort
from flask_jwt import jwt_required
from werkzeug.security import generate_password_hash
import re

email_re = re.compile(r"^[a-zA-Z][\w\.]*@[A-Za-z0-9]+([_\-\.][A-Za-z0-9]+)*\.[a-zA-Z]{2,}")
name_re = re.compile(r"^[a-zA-Z]+([- ][a-zA-Z])*")


@app.route("/api/register", methods=["POST"])
def register():
    if not request.json or not all(key in request.json for key in ["username", "password", "email", "first_name", "last_name", "age"]):
        abort(400, "Not enough arguments")
    user = User()
    for i in request.json:
        if i == "username":
            if len(request.json[i]) > 64:
                abort(400, "Username too long")
            elif User.query.filter_by(username=request.json[i]).all():
                abort(400, "Username already in use")
            user.username = request.json[i]
        elif i == "password":
            user.password = generate_password_hash(request.json[i])
        elif i == "email":
            if not email_re.fullmatch(request.json[i]):
                abort(400, "Email not valid")
            user.email = request.json[i]
        elif i in ["first_name", "last_name"]:
            if not name_re.fullmatch(request.json[i]):
                abort(400, f"{i.title()} invalid")
            setattr(user, i, request.json[i])
        elif i == "age":
            try:
                if 16 >= int(request.json[i]) or int(request.json[i]) >= 30:
                    raise ValueError
            except ValueError:
                abort(400, "Age invalid")
            else:
                user.age = int(request.json[i])
    db.session.add(user)
    db.session.commit()
    return jsonify(UserSchema().dump(user)), 201


@app.route("/api/", methods=["GET"])
@jwt_required()
def root():
    return "ok"
