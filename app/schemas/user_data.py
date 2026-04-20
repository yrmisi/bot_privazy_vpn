from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserData:
    """Telegram user fields passed from middleware into handlers."""

    telegram_id: int
    full_name: str
    is_bot: bool
    language_code: str
    is_premium: bool
    free_trial: datetime
