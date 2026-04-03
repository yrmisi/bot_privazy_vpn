from typing import Annotated

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from .paths import ENVS_DIR


class MessageUserUnauthConfig:
    """Message config for unauthenticated user."""

    key_text: str = "hello_unauth_user_text"
    key_call_data: str = "hello_unauth_user_call_data"
    rows_size: list[int] = [1]


class MessageUserAuthConfig:
    """Message config for authenticated user."""

    key_text: str = "hello_auth_user_text"
    key_call_data: str = "hello_auth_user_call_data"
    rows_size: list[int] = [1, 2, 2, 1]
    key_text_echo: str = "message_echo"


class BotConfig(BaseSettings):
    token: Annotated[SecretStr, Field(alias="BOT_TOKEN")] = SecretStr("")
    local_file_type: str = ".json"
    free_days: int = 3
    msg_unauth: MessageUserUnauthConfig = MessageUserUnauthConfig()
    msg_auth: MessageUserAuthConfig = MessageUserAuthConfig()

    model_config = SettingsConfigDict(
        env_file=ENVS_DIR / ".env.bot",
        env_file_encoding="utf-8",
    )
