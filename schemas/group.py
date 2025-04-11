from marshmallow import fields
from schemas import ma
from models.group import Group


class GroupSchema(ma.SQLAlchemyAutoSchema):

    created_by = fields.Integer(data_key="created_by")
    updated_by = fields.Integer(data_key="updated_by")
    farm_id = fields.Integer(data_key="farm_id")

    class Meta:
        model = Group
        load_instance = True
        include_relationships = True
