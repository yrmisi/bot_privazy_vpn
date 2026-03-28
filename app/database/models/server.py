from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .protocol import Protocol
    from .vpn_subscription import VpnSubscription


# VPN-сервера например Нидерланды #1 или Германия #123
class Server(Base):
    """VPN server model."""

    protocol_id: Mapped[UUID] = mapped_column(
        UUID,
        ForeignKey("protocols.id"),
    )
    name: Mapped[str] = mapped_column(
        String(125),
        nullable=False,
        index=True,
    )
    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    max_connections: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    current_connections: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    server_ip: Mapped[str] = mapped_column(
        String(125),
        nullable=False,
    )
    server_hash: Mapped[str] = mapped_column(
        String(125),
        nullable=False,
    )

    protocol: Mapped["Protocol"] = relationship(back_populates="servers")
    users: Mapped[list["VpnSubscription"]] = relationship(back_populates="vpn")
