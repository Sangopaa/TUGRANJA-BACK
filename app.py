from config import Config

from flask import Flask
from flask_cors import CORS
from url import add_urls

from sqlalchemy import NullPool
from models import db
from schemas import ma

config = Config()

db_name = config.get("MYSQL_DATABASE_DB")
connection_string = f"mysql+pymysql://{config.get('MYSQL_DATABASE_USER')}:{config.get('MYSQL_DATABASE_PASSWORD')}@{config.get('MYSQL_DATABASE_HOST')}:{config.get('MYSQL_DATABASE_PORT')}/{db_name}"


def create_flask_app(use_null_pool=False):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = (
        {"poolclass": NullPool} if use_null_pool else {"pool_recycle": 3600}
    )

    db.init_app(app)
    ma.init_app(app)

    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    CORS(app)

    return app


if __name__ == "__main__":
    app = create_flask_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
