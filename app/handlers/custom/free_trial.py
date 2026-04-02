from aiogram import F, Router
from aiogram.types import CallbackQuery, InaccessibleMessage
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import UserData
from services import UserVPNService

router = Router()


@router.callback_query(F.data == "start_free")
async def get_free_trial_call(
    callback: CallbackQuery,
    user_data: UserData,
    session: AsyncSession,
) -> None:
    """
    Handle free trial activation request.
    """

    msg = callback.message

    # защита от None и InaccessibleMessage
    if msg is None or isinstance(msg, InaccessibleMessage):
        await callback.answer("Сообщение недоступно")
        return

    user_vpn: UserVPNService = UserVPNService(session)
    text: str = await user_vpn.activate_trial(user_data)

    await msg.edit_text(text)
