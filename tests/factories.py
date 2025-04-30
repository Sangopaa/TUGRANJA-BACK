import factory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

from models import db
from models.user import User
from models.farm import Farm

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

    username = faker.user_name()
    email = faker.email()
    farm = factory.SubFactory(FarmFactory)
