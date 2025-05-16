from tests.factories import FarmFactory

from core.farm.farm_service import FarmService

from models import db
from models.farm import Farm

from unittest.mock import patch
import json


class TestFarmDetailViewGetMethod:

    def setup_method(self):
        self.farm = FarmFactory()

    def act(self, farm_id: int, client):
        self.response = client.get(
            f"farm/{farm_id}", headers={"content-type": "application/json"}
        )

        self.response_json = self.response.json
        self.status_code = self.response.status_code

    def test_return_farm_data(self, client):
        self.act(farm_id=self.farm.identifier, client=client)

        assert self.status_code == 200
        assert self.response_json["identifier"] == self.farm.identifier
        assert self.response_json["name"] == self.farm.name
        assert self.response_json["created_at"] == self.farm.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S"
        )
        assert self.response_json["updated_at"] == self.farm.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S"
        )

    def test_return_data_when_farm_does_not_exist(self, client):
        self.act(farm_id=999999, client=client)

        assert self.status_code == 404
        assert self.response_json["error"] == "Farm not found."


class TestFarmViewDetailPostMethod:

    def act(self, payload, client):
        self.response = client.post(
            f"/farm",
            headers={"content-type": "application/json"},
            data=json.dumps(payload),
        )

        self.response_json = self.response.json
        self.status_code = self.response.status_code

    def test_right_creation_farm(self, client):
        self.act(payload={"name": "Farm 1"}, client=client)

        db_result = db.session.query(Farm).filter(Farm.name == "Farm 1").first()

        assert self.status_code == 201
        assert self.response_json["identifier"] == db_result.identifier
        assert self.response_json["name"] == db_result.name
        assert self.response_json["created_at"] == db_result.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S"
        )
        assert self.response_json["updated_at"] == None


class TestFarmViewGetMethod:
    def setup_method(self):
        self.farms = FarmFactory.create_batch(25)

    def act(self, client, query_params=""):
        base_url = "/farms"
        self.response = client.get(
            f"{base_url}?{query_params}" if query_params else base_url,
            headers={"content-type": "application/json"},
        )

        self.response_json = self.response.json
        self.status_code = self.response.status_code

    def test_it_return_status_code_200(self, client):
        self.act(client=client)

        assert self.status_code == 200

    def test_it_return_right_error_when_page_is_not_valid(self, client):
        self.act(client=client, query_params="page=aoeu")

        assert self.status_code == 400
        assert self.response_json["error"] == "Invalid value for argument 'page'"

    def test_it_return_right_error_when_size_is_not_valid(self, client):
        self.act(client=client, query_params="size=aoeu")

        assert self.status_code == 400
        assert self.response_json["error"] == "Invalid value for argument 'size'"

    def test_it_return_404_when_farms_does_not_exist(self, client):
        for farm in self.farms:
            db.session.delete(farm)
        db.session.commit()
        self.act(client=client)

        assert self.status_code == 404
        assert self.response_json["error"] == "No farms found."

    @patch.object(FarmService, "get_farms")
    def test_it_called_get_farms_with_correct_size_and_page(
        self, mock_get_farms, client
    ):
        self.act(client=client, query_params="size=13&page=2")

        mock_get_farms.assert_called_once_with(size=13, page=2)
