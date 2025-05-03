from flask import request
from flask_restful import Resource

from core.farm.farm_service import FarmService


class FarmView(Resource):

    def __init__(self):
        self.farm_service = FarmService()

    def get(self, farm_id: int):
        response = self.farm_service.get_farm(farm_id=farm_id)
        return response.response, response.status_code

    def post(self):
        response = self.farm_service.create_farm(farm_data=request.json)
        return response.response, response.status_code
