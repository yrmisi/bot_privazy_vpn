import subprocess
from functools import cached_property
from typing import Annotated

from aiogram.client.session.aiohttp import AiohttpSession
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
    is_proxy: Annotated[bool, Field(alias="IS_PROXY")] = False
    proxy_url: str = "socks5://{ip_host}:1080"

    model_config = SettingsConfigDict(
        env_file=ENVS_DIR / ".env.bot-prod",
        env_file_encoding="utf-8",
    )

    @cached_property
    def session(self) -> AiohttpSession | None:
        """
        Create an AiohttpSession with a proxy if proxy_url is provided.
        """
        if not self.is_proxy:
            return None

        ip_host: str = self._get_default_gateway_ip()
        return AiohttpSession(proxy=self.proxy_url.format(ip_host=ip_host))

    @staticmethod
    def _get_default_gateway_ip() -> str:
        """
        Get a Windows IP-host address.
        """
        try:
            cmd: str = "ip route show | grep default | awk '{print $3}'"
            return subprocess.check_output(cmd, shell=True).decode().strip()
        except Exception:
            return "127.0.0.1"
