from marshmallow_sqlalchemy import ModelSchema
from app.models import *


class UsersSchema(ModelSchema):
    class Meta:
        model = User
