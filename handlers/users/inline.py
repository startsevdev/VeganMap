import logging
from aiogram import types

from loader import dispatcher
from aiogram.dispatcher import FSMContext

from utils.get_nearest_restaurants import get_nearest_restaurant
from keyboards.inline.restaurant_kb import create_restaurant_kb
from keyboards.inline.send_next_kb import create_send_next_kb
from utils import amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.callback_query_handler(text_contains='send_map')
async def send_map(call: types.CallbackQuery):
    data = call.data.split(":")
    await call.message.answer_location(float(data[1]), float(data[2]))
    await call.message.answer("<b>{}</b>".format(data[3]), reply_markup=create_send_next_kb())

    logging.info("User {} clicked «Open map» under {}".format(call.from_user.id, data[3]))
    amplitude.log_send_map(call.from_user.id)


@dispatcher.callback_query_handler(text_contains='send_next')
async def send_next(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_latitude, user_longitude, user_state = data.get("user_latitude"), data.get("user_longitude"), data.get("state")

    restaurant = get_nearest_restaurant(user_latitude, user_longitude, user_state)
    image_id, text = restaurant.create_message_content(user_latitude, user_longitude)
    await call.message.answer_photo(photo=image_id, caption=text, reply_markup=create_restaurant_kb(
            restaurant.latitude, restaurant.longitude, restaurant.name))

    # await call.message.answer(text="Больше заведений", reply_markup=create_show_more_kb())

    async with state.proxy() as data:
        data["state"] += 1

    logging.info("User {} clicked inline button «Show more»".format(call.from_user.id))
    amplitude.log_send_next(call.from_user.id)

