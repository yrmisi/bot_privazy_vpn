from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .vpn_subscription import VpnSubscription


class User(Base):
    """
    Telegram bot User model.
    """

    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
    )
    full_name: Mapped[str | None] = mapped_column(
        String(250),
        nullable=True,
        index=True,
    )
    is_bot: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    language_code: Mapped[str | None] = mapped_column(
        String(15),
        nullable=True,
        index=True,
    )
    is_premium: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    free_trial: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    subscriptions: Mapped[list["VpnSubscription"]] = relationship(
        back_populates="user",
        lazy="selectin",
    )
