import logging
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dispatcher, amplitude, database
from utils.get_nearest_restaurants import get_nearest_restaurant_id
from keyboards.inline.restaurant_kb import create_restaurant_kb


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION, state="*")
async def location_handler(message: types.Message, state: FSMContext):
    r_id = get_nearest_restaurant_id(message.location.latitude, message.location.longitude, state=0)
    restaurant = database.restaurants[r_id]
    image_id, text = restaurant.create_message_content(message.location.latitude, message.location.longitude)
    await message.answer_photo(photo=image_id, caption=text, reply_markup=create_restaurant_kb(r_id))

    # await message.answer(text="Больше заведений", reply_markup=create_show_more_kb())
    await state.update_data(state=1, suggest_state=0, user_latitude=message.location.latitude, user_longitude=message.location.longitude)

    logging.info("User {} sent location {}, {}".format(
        message.from_user.id, message.location.latitude, message.location.longitude))
    amplitude.log(message.from_user.id, "Location")
