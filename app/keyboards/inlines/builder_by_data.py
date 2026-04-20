from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_kb(
    call_data: list[dict[str, str]],
    data_latest_row: dict[str, str] | None = None,
    rows_size: list[int] | None = None,
) -> InlineKeyboardMarkup:
    """
    Build inline keyboard with customizable row sizes.
    """
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    if rows_size is None:
        rows_size = [1]

    for data in call_data:
        builder.button(
            text=data["text"],
            callback_data=data["callback_data"],
            style=data.get("style", None),
        )

    builder.adjust(*rows_size)

    if data_latest_row:
        builder.row(
            InlineKeyboardButton(
                text=data_latest_row["text"],
                callback_data=data_latest_row["callback_data"],
                style=data.get("style", None),
            )
        )
    return builder.as_markup()
