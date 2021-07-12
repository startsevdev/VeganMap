from aiogram import types

from loader import dispatcher
from utils.get_nearest_restaurants import get_3_nearest_restaurants


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    print(message)
    nearest_restaurants = get_3_nearest_restaurants(message)

    for restaurant in nearest_restaurants:
        image_id, text = restaurant.create_message_content(message)
        await message.answer_photo(photo=image_id, caption=text, parse_mode="HTML")
