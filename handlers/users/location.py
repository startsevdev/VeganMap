from aiogram import types

from loader import dispatcher
from utils.get_nearest_restaurants import get_3_nearest_restaurants
from keyboards.inline.open_map import create_open_map_kb


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    nearest_restaurants = get_3_nearest_restaurants(message)

    for restaurant in nearest_restaurants:
        image_id, text = restaurant.create_message_content(message)
        await message.answer_photo(photo=image_id, caption=text, parse_mode="HTML",
                                   reply_markup=create_open_map_kb("{}, {}".format(restaurant.coords_str, restaurant.name)))

