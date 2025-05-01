from dotenv import dotenv_values


class Config:
    _instance = None

    def __new__(
        cls,
    ):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_config()
        return cls._instance

    def _init_config(self):
        self.config = dotenv_values(dotenv_path=".env")

    def get_env_variable(self, key, default=None):
        return self.config.get(key, default)
