from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, User

from exceptions import UserNotFoundError

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    user: User | None = message.from_user
    if user is None:
        raise UserNotFoundError

    await message.answer(f"Hello, <b>{user.full_name}!</b>")
