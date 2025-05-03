import factory
from factory import Sequence

from faker import Factory as FakerFactory
from pytest_factoryboy import register

from models import db
from models.user import User
from models.farm import Farm
from models.group import Group
from models.variable import Variable
from models.animal import Animal
from models.animal_variable_value import AnimalVariableValue

faker = FakerFactory.create()


@register
class FarmFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Farm
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = faker.name()
    created_at = faker.date_time_this_year()
    updated_at = faker.date_time_this_year()


@register
class UserFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    username = Sequence(lambda n: f"user{n}{faker.user_name()}")
    email = Sequence(lambda n: f"user{n}{faker.email()}")
    farm = factory.SubFactory(FarmFactory)


@register
class GroupFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Group
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = Sequence(lambda n: f"user{n}{faker.name()}")
    created_at = faker.date_time_this_year()
    updated_at = faker.date_time_this_year()
    created_by_user = factory.SubFactory(UserFactory)
    updated_by_user = factory.SubFactory(UserFactory)
    farm = factory.SubFactory(FarmFactory)
    active = True


@register
class VariableFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Variable
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = Sequence(lambda n: f"variable{n}{faker.name()}")
    created_at = faker.date_time_this_year()
    updated_at = faker.date_time_this_year()
    created_by_user = factory.SubFactory(UserFactory)
    updated_by_user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
    active = True


@register
class AnimalFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = Animal
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    name = Sequence(lambda n: f"animal{n}{faker.name()}")
    birth_date = faker.date_time_this_year()
    race = "Race"
    gender = "Male"
    procedence = faker.name()
    created_at = faker.date_time_this_year()
    updated_at = faker.date_time_this_year()
    created_by_user = factory.SubFactory(UserFactory)
    updated_by_user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
    active = True


@register
class AnimalVariableValueFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = AnimalVariableValue
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    value = faker.name()
    created_at = faker.date_time_this_year()
    updated_at = faker.date_time_this_year()
    created_by_user = factory.SubFactory(UserFactory)
    updated_by_user = factory.SubFactory(UserFactory)
    animal = factory.SubFactory(AnimalFactory)
    variable = factory.SubFactory(VariableFactory)
