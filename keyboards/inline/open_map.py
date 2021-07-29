from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_open_map_kb(latitude: float, longitude: float, name: str):
    data = "open_map:{}:{}:{}".format(latitude, longitude, name)

    open_map_button = InlineKeyboardButton("🗺️ Открыть карту", callback_data=data)
    show_more_button = InlineKeyboardButton("🍃 Показать ещё", callback_data="show_more")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(open_map_button)
    keyboard.add(show_more_button)
    return keyboard
