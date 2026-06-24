from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PORT: int = 7100
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/zapisi"
    ADMIN_PASSWORD: str = "admin"

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        if v.startswith("postgresql://"):
            return v.replace("postgresql://", "postgresql+asyncpg://", 1)
        if v.startswith("postgres://"):
            return v.replace("postgres://", "postgresql+asyncpg://", 1)
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
