class TestPingView:

    def act(self, client):
        self.response = client.get("ping", headers={"content-type": "application/json"})

        self.response_json = self.response.json
        self.status_code = self.response.status_code

    def test_it_returns_status_code_200(self, client):
        self.act(client=client)

        assert self.status_code == 200

    def test_it_response_pong(self, client):
        self.act(client=client)

        assert self.response_json["message"] == "pong"

    def test_it_response_only_attribute(self, client):
        self.act(client=client)

        assert len(self.response_json) == 1
