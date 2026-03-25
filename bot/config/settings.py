from pydantic import BaseModel

from .bot import BotConfig


class Settings(BaseModel):
    """Configuration for the application."""

    bot: BotConfig = BotConfig()


settings = Settings()
