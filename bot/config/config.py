from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
    API_KEY: str

    POINTS: list[int] = [700, 900]
    SWIPE_POINTS: list[int] = [2500, 3000]

    USE_REF: bool = False
    REF_ID: str = ""

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
