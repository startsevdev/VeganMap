from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_show_more_kb(user_latitude: float, user_longitude: float):
    data = "show_more:{}:{}".format(user_latitude, user_longitude)
    inline_button = InlineKeyboardButton("Показать ещё", callback_data=data)
    return InlineKeyboardMarkup().add(inline_button)
