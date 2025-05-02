from shared.responses.dict_response import DictResponse
from shared.responses.base_response import BaseResponse


class TestDictResponse:

    def setup_method(self):
        self.response = DictResponse()

    def test_right_inheritance(self):
        assert isinstance(self.response, BaseResponse)
        assert isinstance(self.response, DictResponse)

    def test_right_creation_of_attributes(self):
        assert "status_code" in self.response.__dict__
        assert "response" in self.response.__dict__

    def test_right_default_types(self):
        assert isinstance(self.response.status_code, int)
        assert isinstance(self.response.response, dict)

    def test_right_creation_of_default_values(self):
        assert self.response.status_code == 200
        assert self.response.response == {}

    def test_right_creation_of_custom_values(self):
        custom_response = DictResponse(status_code=404, response={"error": "Not Found"})
        assert custom_response.status_code == 404
        assert custom_response.response == {"error": "Not Found"}
