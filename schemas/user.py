from marshmallow import fields
from schemas import ma
from models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):

    farm_id = fields.Integer(data_key="farm_id")

    class Meta:
        model = User
        load_instance = True
        include_relationships = True
