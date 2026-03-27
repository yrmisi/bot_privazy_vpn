from pydantic import BaseModel

from .bot import BotConfig
from .database import DatabaseConfig


class Settings(BaseModel):
    """Configuration for the application."""

    bot: BotConfig = BotConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
