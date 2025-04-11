from marshmallow import fields
from schemas import ma
from models.farm import Farm


class FarmSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Farm
        load_instance = True
        include_relationships = True
