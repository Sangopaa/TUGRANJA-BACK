from marshmallow import fields
from schemas import ma
from models.variable import Variable


class VariableSchema(ma.SQLAlchemyAutoSchema):

    created_by = fields.Integer(data_key="created_by")
    updated_by = fields.Integer(data_key="updated_by")
    group_id = fields.Integer(data_key="group_id")

    class Meta:
        model = Variable
        load_instance = True
        include_relationships = True
