from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.inlines import build_kb
from schemas import UserAnswer, UserData
from services import UserVPNService

router = Router()


@router.message(CommandStart())
async def command_start_handler(
    message: Message,
    user_data: UserData,
    session: AsyncSession,
) -> None:
    """
    This handler receives messages with `/start` command
    """

    user_vpn: UserVPNService = UserVPNService(session)
    user_answer: UserAnswer = await user_vpn.get_hello_user(user_data)

    kb = build_kb(
        call_data=user_answer.call_data,
        rows_size=user_answer.rows_size,
    )

    await message.answer(user_answer.text, reply_markup=kb)
