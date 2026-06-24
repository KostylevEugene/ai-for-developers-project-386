from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PORT: int = 7100
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/zapisi"
    ADMIN_PASSWORD: str = "admin"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
