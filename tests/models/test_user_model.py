from tests.factories import UserFactory


class TestsUserModel:

    def test_user_model_fields(self):
        user = UserFactory()

        assert user.identifier
        assert "username" in user.__dict__
        assert "email" in user.__dict__
        assert "created_at" in user.__dict__
        assert "updated_at" in user.__dict__
        assert "farm_id" in user.__dict__
