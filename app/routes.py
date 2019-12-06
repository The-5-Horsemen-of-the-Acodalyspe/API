from app import app
from app.schemas import *
from flask import jsonify, request, abort
from flask_jwt import jwt_required, current_identity
from werkzeug.security import generate_password_hash
import re

email_re = re.compile(r"^[a-zA-Z][\w\.]*@[A-Za-z0-9]+([_\-\.][A-Za-z0-9]+)*\.[a-zA-Z]{2,}")
name_re = re.compile(r"^[a-zA-Z]+([- ][a-zA-Z])*")


def set_user(user, request):
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
        elif i == "housing":
            if not user.housing.count():
                user.housing.append(Housing())
            for j in request.json[i]:
                if j == "wholesomeness":
                    if request.json[i][j] is True:
                        b = True
                    elif request.json[i][j] is False:
                        b = False
                    else:
                        abort(400, "Invalid wholesomeness")
                    user.housing[0].wholesomeness = b
                elif j == "price":
                    try:
                        int(request.json[i][j])
                    except ValueError:
                        abort(400, f"Invalid {j}")
                    else:
                        user.housing[0].price = int(request.json[i][j])
                elif j == "typeHousing":
                    s = TypeHousing.query.filter_by(name=request.json[i][j]).first()
                    if s:
                        user.housing[0].type_housing = s
                    else:
                        abort(400, "Invalid typeHousing")

        elif i == "transport":
            if not user.transport.count():
                user.transport.append(Transport())
            for j in request.json[i]:
                if j == "transportTime":
                    try:
                        int(request.json[i][j])
                    except ValueError:
                        abort(400, "Invalid transportTime")
                    else:
                        user.transport[0].transportTime = int(request.json[i][j])
                elif j == "distance":
                    try:
                        float(request.json[i][j])
                    except ValueError:
                        abort(400, "Invalid distance")
                    else:
                        user.transport[0].distance = float(request.json[i][j])
                elif j == "needs_proximity":
                    if request.json[i][j] is True:
                        b = True
                    elif request.json[i][j] is False:
                        b = False
                    else:
                        abort(400, "Invalid needs_proximity")
                        user.transport[0].needs_proximity = b
                elif j == "typeTransport":
                    s = TypeTransport.query.filter_by(name=request.json[i][j]).first()
                    if s:
                        user.transport[0].type_transport = s
                    else:
                        abort(400, "Invalid typeTransport")
        elif i == "study":
            if not user.study.count():
                user.study.append(Study())
            for j in request.json[i]:
                if j in ["level", "douille"]:
                    try:
                        int(request.json[i][j])
                    except ValueError:
                        abort(400, f"Invalid {j}")
                    else:
                        setattr(user.study[0], j, int(request.json[i][j]))
                elif j == "formation":
                    s = Formation.query.filter_by(name=request.json[i][j]).first()
                    if s:
                        user.study[0].formation = s
                    else:
                        abort(400, "Invalid formation")
        elif i == "technology":
            if not user.technology.count():
                user.technology.append(Technology())
            for j in request.json[i]:
                if j in ["hardware", "internet", "printer"]:
                    if request.json[i][j] is True:
                        b = True
                    elif request.json[i][j] is False:
                        b = False
                    else:
                        abort(400, f"Invalid {j}")
                    setattr(user.technology[0], j, b)
        elif i == "finance":
            if not user.finance.count():
                user.finance.append(Finance())
            for j in request.json[i]:
                if j == "work":
                    if request.json[i][j] is True:
                        b = True
                    elif request.json[i][j] is False:
                        b = False
                    else:
                        abort(400, f"Invalid {j}")
                    setattr(user.finance[0], j, b)
                elif j in ["scholarships", "APL", "other", "family"]:
                    try:
                        int(request.json[i][j])
                    except ValueError:
                        abort(400, f"Invalid {j}")
                    else:
                        setattr(user.finance[0], j, int(request.json[i][j]))
        elif i == "handicap":
            if not user.handicap.count():
                user.handicap.append(Handicap())
            if request.json[i] is True:
                b = True
            elif request.json[i] is False:
                b = False
            else:
                abort(400, "Invalid handicap")
            user.handicap[0].handicap = b
        elif i == "family":
            if not user.family.count():
                user.family.append(Family())
            for j in request.json[i]:
                if j in ["death", "divorce", "violence"]:
                    if request.json[i][j] is True:
                        b = True
                    elif request.json[i][j] is False:
                        b = False
                    else:
                        abort(400, f"Invalid {j}")
                    setattr(user.family[0], j, b)
                elif j == "distance":
                    try:
                        int(request.json[i][j])
                    except ValueError:
                        abort(400, f"Invalid {j}")
                    else:
                        user.family[0].distance = int(request.json[i][j])
        elif i == "university":
            s = University.query.filter_by(name=request.json[i]).first()
            if s:
                user.university = s
            else:
                abort(400, "Invalid university")


@app.route("/api/register", methods=["POST"])
def register():
    if not request.json or not all(key in request.json for key in ["username", "password", "email", "first_name", "last_name", "age"]):
        abort(400, "Not enough arguments")
    user = User()
    set_user(user, request)
    db.session.add(user)
    db.session.commit()
    return jsonify(UserSchema().dump(user)), 201


@app.route("/api/user", methods=["PUT"])
@jwt_required()
def update_user():
    set_user(current_identity, request)
    db.session.commit()
    return jsonify(UserSchema().dump(current_identity))


@app.route("/api/", methods=["GET"])
@jwt_required()
def root():
    return "ok"
