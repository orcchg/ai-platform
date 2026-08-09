from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    jwt_secret: str
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
