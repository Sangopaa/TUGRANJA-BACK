from tests.factories import FarmFactory

from model_queries.farm import get_farm_by_id

from models.farm import Farm

import pytest


class TestGetFarmById:

    def setup_method(self):
        self.farm = FarmFactory()

    def test_get_farm_by_id_return_farm_object(self):
        result = get_farm_by_id(farm_id=self.farm.identifier)
        assert isinstance(result, Farm)

    def test_get_farm_by_id_farm_exists(self):
        result = get_farm_by_id(farm_id=self.farm.identifier)
        assert result.identifier == self.farm.identifier

    def test_get_farm_by_id_farm_does_not_exist(self):
        result = get_farm_by_id(farm_id=999)
        assert result is None

    @pytest.mark.parametrize("farm_id", [None, "", "invalid_id", True])
    def test_get_farm_by_id_invalid_id(self, farm_id: any):
        result = get_farm_by_id(farm_id=farm_id)
        assert result is None

    def test_get_farm_by_id_return_right_fields(self):
        result = get_farm_by_id(farm_id=self.farm.identifier)
        assert "identifier" in result.__dict__
        assert "name" in result.__dict__
        assert "created_at" in result.__dict__
        assert "updated_at" in result.__dict__

    def test_get_farm_by_id_return_farm_object_with_correct_values(self):
        result = get_farm_by_id(farm_id=self.farm.identifier)
        assert result.identifier == self.farm.identifier
        assert result.name == self.farm.name
        assert result.created_at == self.farm.created_at
        assert result.updated_at == self.farm.updated_at
