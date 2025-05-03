from tests.factories import VariableFactory


class TestsVariableModel:

    def test_variable_model_fields(self):
        variable = VariableFactory()

        assert variable.identifier
        assert "name" in variable.__dict__
        assert "created_at" in variable.__dict__
        assert "updated_at" in variable.__dict__
        assert "created_by" in variable.__dict__
        assert "updated_by" in variable.__dict__
        assert "group_id" in variable.__dict__
        assert "active" in variable.__dict__
