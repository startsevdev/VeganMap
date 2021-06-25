from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


send_geo = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📍 Отправить местоположение", request_location=True)]],
    resize_keyboard=True,
    one_time_keyboard=False
)
