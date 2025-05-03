from tests.factories import AnimalFactory


class TestsAnimalModel:

    def test_animal_model_fields(self):
        animal = AnimalFactory()

        assert animal.identifier
        assert "name" in animal.__dict__
        assert "birth_date" in animal.__dict__
        assert "race" in animal.__dict__
        assert "gender" in animal.__dict__
        assert "procedence" in animal.__dict__
        assert "created_at" in animal.__dict__
        assert "updated_at" in animal.__dict__
        assert "created_by" in animal.__dict__
        assert "updated_by" in animal.__dict__
        assert "group_id" in animal.__dict__
        assert "active" in animal.__dict__
