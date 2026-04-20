from aiogram import Router
from aiogram.types import Message

from schemas import UserData
from services import UserVPNService

router = Router()


@router.message()
async def echo_handler(message: Message, user_data: UserData) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    user_vpn: UserVPNService = UserVPNService()
    text: str = await user_vpn.get_message_echo(user_data.language_code)
    try:
        await message.answer(text)
    except TypeError:
        await message.answer("Nice try!")
