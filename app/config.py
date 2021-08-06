from pydantic import BaseSettings


class BotConfig(BaseSettings):
    token: str

    class Config:
        allow_mutation = False


class AppConfig(BaseSettings):
    bot: BotConfig

    class Config:
        allow_mutation = False
