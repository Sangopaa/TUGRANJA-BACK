from flask_restful import Api

from views.ping import PingView


def add_urls(app):
    api = Api(app)

    api.add_resource(PingView, "/ping", endpoint="ping")
