import os
from dotenv import load_dotenv


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_config()
        return cls._instance

    def _init_config(self):
        load_dotenv(dotenv_path=".env")
        self.config = os.environ

    def get_env_variable(self, key, default=None):
        return self.config.get(key, default)
