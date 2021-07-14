from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_show_more_kb(data: str):
    inline_button = InlineKeyboardButton("Показать ещё", callback_data=data)
    return InlineKeyboardMarkup().add(inline_button)
