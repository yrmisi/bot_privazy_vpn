from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update, User

from exceptions import UserNotFoundError
from schemas import UserData


class UserDataMiddleware(BaseMiddleware):
    """Injects UserData into handler data from the Telegram user."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        target = event
        if isinstance(event, Update):
            target = event.event
        user: User | None = getattr(target, "from_user", None)
        if user is None:
            raise UserNotFoundError

        data["user_data"] = UserData(
            telegram_id=user.id,
            full_name=user.full_name,
            is_bot=user.is_bot,
            language_code=user.language_code or "language not set",
            is_premium=user.is_premium or False,
        )
        return await handler(event, data)
