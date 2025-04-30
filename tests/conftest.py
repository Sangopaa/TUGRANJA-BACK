from flask import Flask
from sqlalchemy import text
import pytest

from models import db
from url import add_urls
from app import connection_string


def clean_database():
    db.drop_all()


@pytest.fixture(scope="session", autouse=True)
def app():
    application = Flask(__name__)
    application.config["SQLALCHEMY_DATABASE_URI"] = connection_string

    with application.app_context():

        db.init_app(application)
        db.create_all()

        add_urls(application)

        yield application
        db.session.commit()
        db.session.close()

        clean_database()


@pytest.fixture(scope="function", autouse=True)
def reset_session():
    yield
    meta = db.metadata
    db.session.rollback()
    con = db.session.connection()

    con.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
    for table in reversed(meta.sorted_tables):
        con.execute(text(f"DELETE FROM `{table.name}`"))
    con.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
    db.session.expire_all()


@pytest.fixture()
def client(app):
    yield app.test_client()
