from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_send_next_kb():
    inline_button = InlineKeyboardButton("🍃 Следующее место", callback_data="send_next")
    return InlineKeyboardMarkup().add(inline_button)
