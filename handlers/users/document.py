from aiogram import types
import logging

from loader import dispatcher, restaurants_storage
from data.config import ADMINS
from data.restaurants import create_restaurants
from loader import bot


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.message_handler(content_types=types.ContentTypes.DOCUMENT, user_id=ADMINS)
async def document_handler(message: types.Message):
    # ПРИСЛАЛИ ПОЛЬЗОВАТЕЛЕЙ
    if message.document.file_name == "users.csv":
        # скачиваем файл
        await bot.download_file_by_id(message.document.file_id, "data/users.csv")
        logging.info("File users.csv replaced")
        await message.answer("👥 База пользователей для рассылки обновлена")

    # ПРИСЛАЛИ РЕСТОРАНЫ
    elif message.document.file_name[-4:] == ".csv":
        # скачиваем файл
        await bot.download_file_by_id(message.document.file_id, "data/restaurants.csv")
        logging.info("File restaurants.csv replaced")
        # обновляем restaurants (который лежит в loader)
        restaurants_storage.update_restaurants(create_restaurants())
        logging.info("Parsing finished")
        await message.answer("📁 База ресторанов обновлена")

