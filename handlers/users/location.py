from aiogram import types

from loader import dispatcher
from utils.get_nearest_restaurants_on_sphere import get_nearest_restaurant


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    await message.answer(get_nearest_restaurant(message).name)
