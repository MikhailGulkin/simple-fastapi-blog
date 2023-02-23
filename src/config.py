from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str

    class Config:
        env_file = '.dev.env'


def get_settings() -> Settings:
    return Settings()
