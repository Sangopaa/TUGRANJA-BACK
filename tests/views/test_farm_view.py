from tests.factories import FarmFactory
import json

from models import db
from models.farm import Farm


class TestFarmViewGetMethod:

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


class TestFarmViewPostMethod:

    def act(self, payload, client):
        self.response = client.post(
            f"farm",
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
