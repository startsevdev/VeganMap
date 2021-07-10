from aiogram import types

from loader import dispatcher
from utils.get_nearest_restaurants import get_3_nearest_restaurants
from utils import message_content


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    nearest_restaurants = get_3_nearest_restaurants(message)
    for restaurant in nearest_restaurants:
        print(restaurant.name, restaurant.image_link)
        image, text = message_content.get_restaurant_content(restaurant)
        await message.answer_photo(photo=image, caption=text)
