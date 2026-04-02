import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from core.i18n import load_translations_to_cache
from handlers.custom import free_router
from handlers.default import echo_router, start_router
from middlewares import include_middleware


async def main() -> None:
    """
    Initialize dispatcher, setup middleware and routers, and start bot polling.
    """
    dp = Dispatcher()

    dp.include_routers(
        start_router,
        free_router,
        echo_router,
    )
    await include_middleware(dp)

    bot = Bot(
        token=settings.bot.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    load_translations_to_cache()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
