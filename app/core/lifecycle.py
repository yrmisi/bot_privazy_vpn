import logging

from aiogram import Bot

from config import settings
from core.i18n import load_translations_to_cache
from database import async_engine


async def on_startup(bot: Bot) -> None:
    """
    Initialize data when starting the bot.
    """
    load_translations_to_cache()
    logging.info("Translations loaded to cache.")


async def on_shutdown(bot: Bot) -> None:
    """
    Correct termination: closing the connection.
    """
    if settings.bot.session:
        logging.info("Closing aiohttp session.")
        await settings.bot.session.close()

    logging.info("Closing database connection.")
    await async_engine.dispose()
