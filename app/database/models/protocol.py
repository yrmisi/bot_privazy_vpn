from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .server import Server


class Protocol(Base):
    """Model representing a VPN protocol (e.g., VLESS, Shadowsocks, OpenVPN, WireGuard)."""

    name: Mapped[str] = mapped_column(
        String(25),
        nullable=False,
    )

    # отношение к VPN-серверам
    vpns: Mapped[list["Server"]] = relationship(back_populates="protocol")
