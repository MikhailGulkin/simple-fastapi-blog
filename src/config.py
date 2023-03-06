from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    DB_URL: str

    class Config:
        if os.getenv('PROD'):
            env_file = '.env'
        elif os.getenv('TEST'):
            env_file = '.test.env'
        else:
            env_file = '.dev.env'


def get_settings() -> Settings:
    return Settings()
