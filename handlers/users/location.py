from aiogram import types

from loader import dispatcher
from utils.get_nearest_restaurants import get_3_nearest_restaurants


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    nearest_restaurants = get_3_nearest_restaurants(message)
    await message.answer("{0}, {1}, {2}".format(nearest_restaurants[0].name, nearest_restaurants[1].name, nearest_restaurants[2].name))
