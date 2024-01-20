from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = Field(
        "default app name",
        description="default app name",
    )

    ADMIN_EMAIL: str = Field(
        "admin@test.test",
        description="admin email",
    )

    model_config = SettingsConfigDict(env_file='.env')


SETTINGS = Settings()
