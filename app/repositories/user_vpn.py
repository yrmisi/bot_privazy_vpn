from dataclasses import asdict

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User
from schemas import UserData


class UserVPNRepository:
    """
    Repository for user VPN operations.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, user_tg_id: int) -> User | None:
        """
        Get user from database by telegram_id.
        """
        return await self.session.scalar(select(User).where(User.telegram_id == user_tg_id))

    async def add(self, user_data: UserData) -> None:
        """ """
        user: User = User(**asdict(user_data))
        self.session.add(user)
        await self.session.commit()
