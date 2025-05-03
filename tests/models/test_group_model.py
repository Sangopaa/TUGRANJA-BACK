from tests.factories import GroupFactory


class TestsGroupModel:

    def test_group_model_fields(self):
        group = GroupFactory()

        assert group.identifier
        assert "name" in group.__dict__
        assert "created_at" in group.__dict__
        assert "updated_at" in group.__dict__
        assert "created_by" in group.__dict__
        assert "updated_by" in group.__dict__
        assert "farm_id" in group.__dict__
        assert "active" in group.__dict__
