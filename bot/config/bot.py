from typing import Annotated

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from .paths import ENVS_DIR


class BotConfig(BaseSettings):
    token: Annotated[SecretStr, Field(alias="BOT_TOKEN")] = SecretStr("")

    model_config = SettingsConfigDict(
        env_file=ENVS_DIR / ".env.bot",
        env_file_encoding="utf-8",
    )
