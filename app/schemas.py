from marshmallow_sqlalchemy import ModelSchema
from app.models import *


class UsersSchema(ModelSchema):
    class Meta:
        model = User


class HousingSchema(ModelSchema):
    class Meta:
        model = Housing


class TypeHousingSchema(ModelSchema):
    class Meta:
        model = TypeHousing


class TypeTransportSchema(ModelSchema):
    class Meta:
        model = TypeTransport


class StudySchema(ModelSchema):
    class Meta:
        model = Study


class FormationSchema(ModelSchema):
    class Meta:
        model = Formation


class UniversitySchema(ModelSchema):
    class Meta:
        model = University


class TechnologySchema(ModelSchema):
    class Meta:
        model = Technology


class FinanceSchema(ModelSchema):
    class Meta:
        model = Finance


class HandicapSchema(ModelSchema):
    class Meta:
        model = Handicap


class FamilySchema(ModelSchema):
    class Meta:
        model = Family
