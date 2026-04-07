from typing import Annotated

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from .paths import ENVS_DIR


class BotConfig(BaseSettings):
    """
    Bot configuration settings.
    """

    token: Annotated[SecretStr, Field(alias="BOT_TOKEN")] = SecretStr("")
    local_file_type: str = ".json"
    free_days: int = 3

    model_config = SettingsConfigDict(
        env_file=ENVS_DIR / ".env.bot",
        env_file_encoding="utf-8",
    )
