from marshmallow import fields
from schemas import ma
from models.animal import Animal


class AnimalSchema(ma.SQLAlchemyAutoSchema):

    created_by = fields.Integer(data_key="created_by")
    updated_by = fields.Integer(data_key="updated_by")
    group_id = fields.Integer(data_key="group_id")

    class Meta:
        model = Animal
        load_instance = True
        include_relationships = True
