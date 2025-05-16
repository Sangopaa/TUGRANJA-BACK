from tests.factories import AnimalVariableValueFactory


class TestsAnimalVariableValueModel:

    def test_animal_varialbe_value_model_fields(self):
        animal = AnimalVariableValueFactory()

        assert animal.identifier
        assert "value" in animal.__dict__
        assert "created_at" in animal.__dict__
        assert "updated_at" in animal.__dict__
        assert "created_by" in animal.__dict__
        assert "updated_by" in animal.__dict__
        assert "animal_id" in animal.__dict__
        assert "variable_id" in animal.__dict__
