from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_restaurant_kb(latitude: float, longitude: float, name: str):
    data = "send_map:{}:{}:{}".format(latitude, longitude, name)
    print(f"{data} ({len(data.encode('utf-8'))})")

    open_map_button = InlineKeyboardButton("🗺️ Открыть карту", callback_data=data)
    show_more_button = InlineKeyboardButton("🍃 Следующее место", callback_data="send_next")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(open_map_button)
    keyboard.add(show_more_button)

    return keyboard
