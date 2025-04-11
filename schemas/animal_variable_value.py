from marshmallow import fields
from schemas import ma
from models.animal_variable_value import AnimalVariableValue


class AnimalVariableValueSchema(ma.SQLAlchemyAutoSchema):

    variable_id = fields.Integer(data_key="variable_id")
    animal_id = fields.Integer(data_key="animal_id")
    created_by = fields.Integer(data_key="created_by")
    updated_by = fields.Integer(data_key="updated_by")

    class Meta:
        model = AnimalVariableValue
        load_instance = True
        include_relationships = True
