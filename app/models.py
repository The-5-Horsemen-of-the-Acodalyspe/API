from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    university_id = db.Column(db.Integer, db.ForeignKey("university.id"))

    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)

    housing = db.relationship("Housing", backref="user", lazy="dynamic")
    transport = db.relationship("Transport", backref="user", lazy="dynamic")
    study = db.relationship("Study", backref="user", lazy="dynamic")
    technology = db.relationship("Technology", backref="user", lazy="dynamic")
    finance = db.relationship("Finance", backref="user", lazy="dynamic")
    handicap = db.relationship("Handicap", backref="user", lazy="dynamic")
    family = db.relationship("Family", backref="user", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"


class Housing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    typeHousing_id = db.Column(db.Integer, db.ForeignKey("type_housing.id"))

    price = db.Column(db.Integer)
    wholesomeness = db.Column(db.Boolean)

    percent = db.Column(db.Float)

    def __repr__(self):
        return f"<Housing {self.id}>"


class TypeHousing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

    housing = db.relationship("Housing", backref="type_housing", lazy="dynamic")

    def __repr__(self):
        return f"<TypeHousing {self.id}>"


class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    typeTransport_id = db.Column(db.Integer, db.ForeignKey("type_transport.id"))

    transportTime = db.Column(db.Integer)
    distance = db.Column(db.Float)
    needs_proximity = db.Column(db.Boolean)

    percent = db.Column(db.Float)

    def __repr__(self):
        return f"<Transport {self.id}>"


class TypeTransport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.Text)

    housing = db.relationship("Transport", backref="type_transport", lazy="dynamic")

    def __repr__(self):
        return f"<TypeTransport {self.id}>"


class Study(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    formation_id = db.Column(db.Integer, db.ForeignKey("formation.id"))

    level = db.Column(db.Integer)
    douille = db.Column(db.Integer)

    percent = db.Column(db.Float)

    def __repr__(self):
        return f"<Study {self.id}>"


class Formation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)

    study = db.relationship("Study", backref="formation", lazy="dynamic")

    def __repr__(self):
        return f"<Formation {self.id}>"


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    user = db.relationship("User", backref="university", lazy="dynamic")

    def __repr__(self):
        return f"<University {self.id}>"


class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    hardware = db.Column(db.Boolean)
    printer = db.Column(db.Boolean)
    internet = db.Column(db.Boolean)

    percent = db.Column(db.Float)

    def __repr__(self):
        return f"<Technology {self.id}>"


class Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    scholarships = db.Column(db.Integer)
    APL = db.Column(db.Integer)
    other = db.Column(db.Integer)
    family = db.Column(db.Integer)
    work = db.Column(db.Boolean)

    percent = db.Column(db.Float)

    def __repr__(self):
        return f"<Finance {self.id}>"


class Handicap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    handicap = db.Column(db.Boolean)

    percent = db.Column(db.Float)

    def __repr__(self):
        return f"<Handicap {self.id}>"


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    death = db.Column(db.Boolean)
    divorce = db.Column(db.Boolean)
    distance = db.Column(db.Integer)
    violence = db.Column(db.Boolean)

    percent = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Family {self.id}>"
