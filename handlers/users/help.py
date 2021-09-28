from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
import logging

from loader import dispatcher, amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("📍 Отправьте геопозицию, в ответ Vegan Map пришлёт три ближайшие заведения\n\n"
            "🍃 Найти больше мест – по кнопке «Показать ещё»\n\n"
            "🗺️ Проложить маршрут – по кнопке «Открыть карту» под сообщением заведения\n\n"
            "❤️ Предложить заведение – /suggest\n\n"
            "✉️ Вопросы и пожелания – @startsevdev")
    await message.answer(text)

    logging.info("User {} sent /help".format(message.from_user.id))
    amplitude.log(message.from_user.id, "/help")
