from flask_sqlalchemy import SQLAlchemy
from models.base import Base

from models.farm import Farm
from models.user import User
from models.group import Group
from models.variable import Variable
from models.animal import Animal
from models.animal_variable_value import AnimalVariableValue


db = SQLAlchemy(model_class=Base)

__all__ = ["Farm", "User", "Group", "Variable", "Animal", "AnimalVariableValue"]
