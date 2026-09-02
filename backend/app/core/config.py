from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "SentinelX"
    APP_ENV: str = "development"
    APP_VERSION: str = "0.1.0"

    DATABASE_URL: str

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()