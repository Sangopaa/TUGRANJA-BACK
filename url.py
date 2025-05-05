from flask_restful import Api

from views.ping import PingView
from views.farm import FarmView, FarmDetailView


def add_urls(app):
    api = Api(app)

    api.add_resource(PingView, "/ping", endpoint="ping")
    api.add_resource(FarmView, "/farm", "/farm", endpoint="farm")
    api.add_resource(FarmDetailView, "/farm/<int:farm_id>", endpoint="farm_detail")
