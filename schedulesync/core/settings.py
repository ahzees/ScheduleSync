from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "schedulesync"
    ASYNC_DATABASE_URL: str
    SECRET: str
    SECRET_PASSWORD_TOKEN: str

    class Config:
        env_file = ".env"
