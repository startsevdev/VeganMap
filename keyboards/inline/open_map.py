from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_open_map_kb(data: str):
    inline_button = InlineKeyboardButton("🗺️ Открыть карту", callback_data=data)
    return InlineKeyboardMarkup().add(inline_button)
