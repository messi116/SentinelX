from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "SentinelX"
    APP_ENV: str = "development"
    APP_VERSION: str = "0.1.0"

    DATABASE_URL: str

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000

    WAZUH_URL: str
    WAZUH_USERNAME: str
    WAZUH_PASSWORD: str

    WAZUH_INDEXER_URL: str | None = None
    WAZUH_INDEXER_USERNAME: str | None = None
    WAZUH_INDEXER_PASSWORD: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()