from flask import request
from flask_restful import Resource

from core.farm.farm_service import FarmService
from shared.utils.get_request_arg import get_int_request_arg


class FarmView(Resource):

    def __init__(self):
        self.farm_service = FarmService()

    def get(self):

        try:
            size = get_int_request_arg(args=request.args, arg_name="size", default=10)
            page = get_int_request_arg(args=request.args, arg_name="page", default=1)

        except Exception as e:
            return {"error": str(e)}, 400

        response = self.farm_service.get_farms(size=size, page=page)
        return response.response, response.status_code


class FarmDetailView(Resource):

    def __init__(self):
        self.farm_service = FarmService()

    def get(self, farm_id: int):
        response = self.farm_service.get_farm(farm_id=farm_id)
        return response.response, response.status_code

    def post(self):
        response = self.farm_service.create_farm(farm_data=request.json)
        return response.response, response.status_code
