from tests.factories import FarmFactory

from core.farm.farm_service import FarmService

from schemas.farm import FarmSchema
from shared.utils.handler_exception import DictResponse

from unittest.mock import patch
import pytest

from models import db
from models.farm import Farm


class TestFarmService:
    def setup_method(self):
        self.farm = FarmFactory()
        self.farm_service = FarmService()

    def test_farm_service_initialization_sets_up_schema_and_response(self):
        assert isinstance(self.farm_service.farm_schema, FarmSchema)
        assert isinstance(self.farm_service.response, DictResponse)


class TestFarmServiceGetFarm:

    def setup_method(self):
        self.farm = FarmFactory()
        self.farm_service = FarmService()

    def test_get_farm_returns_dict_response_for_existing_farm(self):
        response = self.farm_service.get_farm(farm_id=self.farm.identifier)

        assert isinstance(response, DictResponse)

    @pytest.mark.parametrize("farm_id", [None, 9999, -1])
    def test_get_farm_always_returns_dict_response_for_any_farm_id(self, farm_id):
        response = self.farm_service.get_farm(farm_id=farm_id)

        assert isinstance(response, DictResponse)

    def test_get_farm_returns_error_for_missing_farm_id(self):
        response = self.farm_service.get_farm(farm_id=None)

        assert response.status_code == 400
        assert response.response == {"error": "Farm ID is required."}

    def test_get_farm_returns_not_found_error_for_nonexistent_farm_id(self):
        response = self.farm_service.get_farm(farm_id=9999)

        assert response.status_code == 404
        assert response.response == {"error": "Farm not found."}

    def test_get_farm_returns_correct_farm_details_for_existing_farm(self):
        response = self.farm_service.get_farm(farm_id=self.farm.identifier)

        assert response.status_code == 200
        assert len(response.response) == 4
        assert response.response["identifier"] == self.farm.identifier
        assert response.response["name"] == self.farm.name
        assert response.response["created_at"] == self.farm.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S"
        )
        assert response.response["updated_at"] == self.farm.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S"
        )

    @patch("core.farm.farm_service.get_farm_by_id")
    def test_get_farm_calls_get_farm_by_id_with_correct_id_on_success(
        self, mock_get_farm_by_id
    ):
        self.farm_service.get_farm(farm_id=self.farm.identifier)

        mock_get_farm_by_id.assert_called_once_with(farm_id=self.farm.identifier)


class TestFarmServiceCreateFarm:

    def setup_method(self):
        self.farm_service = FarmService()
        self.farm_data = {"name": "Test Farm"}

    def test_create_farm_returns_dict_response_on_success(self):
        response = self.farm_service.create_farm(farm_data=self.farm_data)

        assert isinstance(response, DictResponse)

    @pytest.mark.parametrize("data", [{"other_attribute": "test attribute"}, {}, []])
    def test_create_farm_returns_dict_response_with_edge_cases(self, data):
        response = self.farm_service.get_farm(farm_id=data)

        assert isinstance(response, DictResponse)

    def test_create_farm_returns_right_data_on_success(self):
        response = self.farm_service.create_farm(farm_data=self.farm_data)

        db_result = (
            db.session.query(Farm)
            .filter(Farm.identifier == response.response["identifier"])
            .first()
        )

        assert response.status_code == 201
        assert len(response.response) == 4
        assert response.response["identifier"] == db_result.identifier
        assert response.response["name"] == db_result.name
        assert response.response["created_at"] == db_result.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S"
        )
        assert response.response["updated_at"] == None

    def test_right_creation_in_db(self):
        response = self.farm_service.create_farm(farm_data=self.farm_data)

        db_result = (
            db.session.query(Farm)
            .filter(Farm.identifier == response.response["identifier"])
            .first()
        )

        assert db_result is not None
        assert db_result.name == response.response["name"]
