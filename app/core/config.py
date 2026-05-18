from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"
if not ENV_FILE.exists():
    ENV_FILE = ROOT_DIR.parent / ".env"


class Settings(BaseSettings):
    app_name: str
    app_env: str

    database_url: str

    access_token_secret: str
    refresh_token_secret: str
    jwt_algorithm: str

    access_token_expire_minutes: int
    refresh_token_expire_days: int

    redis_url: str

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE),
        env_file_encoding="utf-8",
    )


settings = Settings()
