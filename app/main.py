import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.default import echo_router, start_router
from middlewares import DbSessionMiddleware, UserDataMiddleware

from config import settings
from database import session_pool


async def main() -> None:
    """Initialize dispatcher, setup middleware and routers, and start bot polling."""

    dp = Dispatcher()

    dp.update.middleware(DbSessionMiddleware(session_pool))
    dp.message.middleware(UserDataMiddleware())
    dp.include_routers(
        start_router,
        echo_router,
    )
    bot = Bot(
        token=settings.bot.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
