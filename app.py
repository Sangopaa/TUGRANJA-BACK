from config import Config

from flask import Flask
from flask_cors import CORS
from url import add_urls

config = Config()


def create_flask_app():
    app = Flask(__name__)
    app_context = app.app_context()
    app_context.push()
    add_urls(app)
    CORS(app)

    return app


if __name__ == "__main__":
    app = create_flask_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
