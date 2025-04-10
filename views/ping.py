from flask_restful import Resource
from config import Config


class PingView(Resource):
    def get(self):
        config_instance = Config()
        secret_key = config_instance.get("SECRET_KEY")
        print(secret_key)
        return {"ping": "pong"}, 200
