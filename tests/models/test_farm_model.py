from tests.factories import FarmFactory


class TestsFarmModel:

    def test_farm_model_fields(self):
        farm = FarmFactory()

        assert farm.identifier
        assert "name" in farm.__dict__
        assert "created_at" in farm.__dict__
        assert "updated_at" in farm.__dict__
