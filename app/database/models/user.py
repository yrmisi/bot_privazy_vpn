from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .vpn_subscription import VpnSubscription


class User(Base):
    """Telegram bot User model."""

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )
    free_period: Mapped[datetime] = mapped_column(DateTime)

    # отношение к VPN-подключениям
    vpns: Mapped[list["VpnSubscription"]] = relationship(back_populates="user")
