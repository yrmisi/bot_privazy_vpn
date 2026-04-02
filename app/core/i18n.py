import json
import os
from typing import Any

from config import settings
from config.paths import LOCALES_DIR

translations_cache: dict[str, dict[str, Any]] = {}


def load_translations_to_cache() -> None:
    """
    Loads translations into cache.
    """
    for lang_file in os.listdir(LOCALES_DIR):
        if lang_file.endswith(settings.bot.local_file_type):
            lang: str = lang_file[:-5]
            with open(
                LOCALES_DIR / f"{lang}{settings.bot.local_file_type}",
                "r",
                encoding="utf-8",
            ) as f:
                translations_cache[lang] = json.load(f)
