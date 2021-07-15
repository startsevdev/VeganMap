from aiogram import types
from loader import dispatcher
from aiogram.dispatcher import FSMContext

from utils.get_nearest_restaurants import get_next_3_nearest_restaurants
from keyboards.inline.open_map import create_open_map_kb


@dispatcher.callback_query_handler(text_contains='open_map')
async def send_map(call: types.CallbackQuery):
    data = call.data.split(":")
    await call.message.answer_location(float(data[1]), float(data[2]))
    await call.message.answer("<b>{}</b>".format(data[3]))


@dispatcher.callback_query_handler(text_contains='show_more')
async def show_more(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_latitude, user_longitude = data.get("user_latitude"), data.get("user_longitude")

    nearest_restaurants = get_next_3_nearest_restaurants(user_latitude, user_longitude)

    for restaurant in nearest_restaurants:
        image_id, text = restaurant.create_message_content(user_latitude, user_longitude)
        await call.message.answer_photo(photo=image_id, caption=text, reply_markup=create_open_map_kb(
            restaurant.latitude, restaurant.longitude, restaurant.name))

    await call.message.answer(data.get("state"))
