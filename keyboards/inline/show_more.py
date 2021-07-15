from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_show_more_kb():
    inline_button = InlineKeyboardButton("Показать ещё", callback_data="show_more")
    return InlineKeyboardMarkup().add(inline_button)
