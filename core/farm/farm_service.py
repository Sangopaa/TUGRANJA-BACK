from shared.responses.dict_response import DictResponse
from shared.utils.handler_exception import handler_service_exceptions

from schemas.farm import FarmSchema

from models import db
from model_queries.farm import get_farm_by_id, get_paginated_farms


class FarmService:

    def __init__(self) -> None:
        self.response = DictResponse()
        self.farm_schema = FarmSchema()

    @handler_service_exceptions
    def get_farm(self, farm_id: int) -> DictResponse:
        """Obtain a farm by its ID.

        Keyword arguments:
            farm_id -- ID of the farm to be obtained.
        Return:
            Response object with the farm data or error message.
        """

        if farm_id is None:
            self.response.status_code = 400
            self.response.response = {"error": "Farm ID is required."}
            return self.response

        farm = get_farm_by_id(farm_id=farm_id)

        if farm is None:
            self.response.status_code = 404
            self.response.response = {"error": "Farm not found."}
            return self.response

        self.response.response = self.farm_schema.dump(farm)
        self.response.status_code = 200

        return self.response

    @handler_service_exceptions
    def get_farms(self, size: int, page: int) -> DictResponse:
        """Obtain all farms.

        Return:
            Response object with the list of farms or error message.
        """

        if size is None or page is None:
            self.response.status_code = 400
            self.response.response = {"error": "Size and page are required."}
            return self.response

        farms, total = get_paginated_farms(page=page, size=size)

        if not farms:
            self.response.status_code = 404
            self.response.response = {"error": "No farms found."}
            return self.response

        self.response.response = {
            "results": self.farm_schema.dump(farms, many=True),
            "total": total,
        }
        self.response.status_code = 200

        return self.response

    @handler_service_exceptions
    def create_farm(self, farm_data: dict) -> DictResponse:
        """Create a new farm.

        Keyword arguments:
            farm_data -- Data of the farm to be created.
        Return:
            Response object with the farm data or error message.
        """

        farm = self.farm_schema.load(farm_data)
        db.session.add(farm)
        db.session.commit()

        self.response.response = self.farm_schema.dump(farm)
        self.response.status_code = 201

        return self.response
