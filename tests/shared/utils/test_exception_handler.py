from unittest.mock import Mock, patch
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from shared.utils.handler_exception import handler_service_exceptions
from shared.responses.dict_response import DictResponse

from models import db


class TestExceptionHandlerDecorator:

    def test_successful_execution(self):
        mock_func = Mock(return_value="Success")
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        mock_func.assert_called_once()
        assert result == "Success"

    def test_return_right_attributes_when_execute_validation_error(self):
        mock_func = Mock(side_effect=ValidationError("Validation error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert "status_code" in result.__dict__
        assert "response" in result.__dict__
        assert "error" in result.response

    def test_return_right_types_when_execute_validation_error(self):
        mock_func = Mock(side_effect=ValidationError("Validation error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert isinstance(result, DictResponse)
        assert isinstance(result.status_code, int)
        assert isinstance(result.response, dict)

    def test_return_right_values_when_execute_validation_error(self):
        mock_func = Mock(side_effect=ValidationError("Validation error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert result.status_code == 400
        assert result.response["error"] == ["Validation error"]

    def test_return_right_attributes_when_execute_integrity_error(self):
        mock_func = Mock(side_effect=IntegrityError(None, None, "Integrity error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert "status_code" in result.__dict__
        assert "response" in result.__dict__
        assert "error" in result.response

    def test_right_types_when_execute_integrity_error(self):
        mock_func = Mock(side_effect=IntegrityError(None, None, "Integrity error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert isinstance(result, DictResponse)
        assert isinstance(result.status_code, int)
        assert isinstance(result.response, dict)

    def test_return_right_values_when_execute_integrity_error(self):
        mock_func = Mock(side_effect=IntegrityError(None, None, "Integrity error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert result.status_code == 400
        assert result.response["error"] == "Integrity error"

    @patch.object(db, "session")
    def test_execute_rollback_when_execute_integrity_error(self, mock_session):
        mock_func = Mock(side_effect=IntegrityError(None, None, "Integrity error"))
        decorated_func = handler_service_exceptions(mock_func)

        decorated_func()

        mock_session.rollback.assert_called_once()

    def test_return_right_attributes_when_execute_generic_exception(self):
        mock_func = Mock(side_effect=Exception("Generic error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert "status_code" in result.__dict__
        assert "response" in result.__dict__
        assert "error" in result.response

    def test_right_types_when_execute_generic_exception(self):
        mock_func = Mock(side_effect=Exception("Generic error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert isinstance(result, DictResponse)
        assert isinstance(result.status_code, int)
        assert isinstance(result.response, dict)

    def test_return_right_values_when_execute_generic_exception(self):
        mock_func = Mock(side_effect=Exception("Generic error"))
        decorated_func = handler_service_exceptions(mock_func)

        result = decorated_func()

        assert result.status_code == 400
        assert result.response["error"] == "Generic error"
