import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp_socks import ProxyConnectionError, ProxyError

from config import settings
from core.lifecycle import on_shutdown, on_startup
from handlers.custom import free_router
from handlers.default import echo_router, start_router
from middlewares import include_middlewares


async def main() -> None:
    """
    Initialize dispatcher, setup middleware and routers, and start bot polling.
    """
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    include_middlewares(dp)

    dp.include_routers(
        start_router,
        free_router,
        echo_router,
    )

    bot = Bot(
        token=settings.bot.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        session=settings.bot.session,
    )

    try:
        await dp.start_polling(bot)
    except ProxyConnectionError as exc:
        logging.critical(f"Proxy connection error: {exc}")
    except ProxyError as exc:
        logging.critical(f"Proxy error: {exc}")
    except Exception as exc:
        logging.critical(f"Unknown error: {exc}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
