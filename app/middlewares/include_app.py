from aiogram import Dispatcher

from database import session_pool

from .db_session import DbSessionMiddleware
from .user_data import UserDataMiddleware


async def include_middleware(dp: Dispatcher) -> None:
    """
    Register all application middlewares.
    """
    dp.update.outer_middleware(DbSessionMiddleware(session_pool))
    dp.message.middleware(UserDataMiddleware())
