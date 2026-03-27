from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import UUID, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .server import Server
    from .user import User


class VpnSubscription(Base):
    """User VPN subscription."""

    __tablename__: str = "vpn_subscriptions"

    user_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey("users.id"),
    )
    vpn_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey("servers.id"),
    )
    paid_before: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    user: Mapped["User"] = relationship(back_populates="vpns")
    vpn: Mapped["Server"] = relationship(back_populates="users")
