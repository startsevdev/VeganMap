from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dispatcher


@dispatcher.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("📍 Отправьте геопозицию, в ответ Vegan Map пришлёт три ближайшие заведения\n\n"
            "🗺️ Проложить маршрут можно по кнопке «Открыть карту» под сообщением заведения\n\n"
            "🍃 Найти больше мест – по кнопке «Показать ещё»\n\n"
            "✉️ Вопросы и предложения отправляйте @startsevdev")
    await message.answer(text)
