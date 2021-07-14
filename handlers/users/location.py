from aiogram import types

from loader import dispatcher
from utils.get_nearest_restaurants import get_3_nearest_restaurants
from keyboards.inline.open_map import create_open_map_kb
from keyboards.inline.show_more import create_show_more_kb


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    nearest_restaurants = get_3_nearest_restaurants(message)

    for restaurant in nearest_restaurants:
        image_id, text = restaurant.create_message_content(message)
        await message.answer_photo(photo=image_id, caption=text, reply_markup=create_open_map_kb(
            "open_map:{}:{}:{}".format(restaurant.latitude, restaurant.longitude, restaurant.name)))
    await message.answer(text="<b>Больше заведений:</b>", reply_markup=create_show_more_kb(
        "show_more:{}:{}".format(message.location.latitude, message.location.longitude)))

