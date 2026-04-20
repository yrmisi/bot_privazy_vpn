from pydantic import BaseModel

from .bot import BotConfig
from .database import DatabaseConfig
from .message_callback_data import MessageCallbackConfig


class Settings(BaseModel):
    """Configuration for the application."""

    bot: BotConfig = BotConfig()
    db: DatabaseConfig = DatabaseConfig()
    msg: MessageCallbackConfig = MessageCallbackConfig()


settings = Settings()
