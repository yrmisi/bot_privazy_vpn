from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from core.i18n import translations_cache
from database.models import User
from repositories import UserVPNRepository
from schemas import UserAnswer, UserData


class UserVPNService:
    """
    Service for VPN server operations.
    """

    def __init__(self, session: AsyncSession | None = None) -> None:
        if isinstance(session, AsyncSession):
            self.repo: UserVPNRepository = UserVPNRepository(session)

    async def get_hello_user(
        self,
        user_data: UserData,
    ) -> UserAnswer:
        """
        Get welcome message data for user.
        """
        user: User | None = await self.repo.get_by_id(user_data.telegram_id)
        trans: dict[str, Any] = await self._get_trans_lang(user_data.language_code)

        if user:
            key_text: str = settings.msg.key_auth_text
            key_call_data: str = settings.msg.key_auth_call_data
            row_size: list[int] = settings.msg.auth_rows_size
        else:
            key_text = settings.msg.key_unauth_text
            key_call_data = settings.msg.key_unauth_call_data
            row_size = settings.msg.unauth_rows_size

        return UserAnswer(
            text="".join(trans[key_text]).format(full_name=user_data.full_name),
            call_data=trans[key_call_data],
            rows_size=row_size,
        )

    async def activate_trial(
        self,
        user_data: UserData,
    ) -> str:
        """
        Activate free trial for user and return success message.
        """
        await self.repo.add(user_data)
        trans: dict[str, Any] = await self._get_trans_lang(user_data.language_code)

        return "".join(trans["successful_free_trial_text"])

    @classmethod
    async def get_message_echo(
        cls,
        lang: str,
    ) -> str:
        """
        Return echo message text for the specified language.
        """
        trans: dict[str, Any] = await cls._get_trans_lang(lang)

        return "".join(trans[settings.msg.key_echo_text])

    @staticmethod
    async def _get_trans_lang(language: str) -> dict[str, Any]:
        """
        Select language code (ru or en).
        """
        lang: str = language if language == "ru" else "en"
        trans: dict[str, Any] = translations_cache[lang]
        return trans
