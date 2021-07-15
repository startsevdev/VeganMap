from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_open_map_kb(latitude: float, longitude: float, name: str):
    data = "open_map:{}:{}:{}".format(latitude, longitude, name)
    inline_button = InlineKeyboardButton("🗺️ Открыть карту", callback_data=data)
    return InlineKeyboardMarkup().add(inline_button)
