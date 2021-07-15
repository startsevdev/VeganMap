from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dispatcher
from utils.get_nearest_restaurants import get_3_nearest_restaurants
from keyboards.inline.open_map import create_open_map_kb
from keyboards.inline.show_more import create_show_more_kb


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dispatcher.message_handler(content_types=types.ContentTypes.LOCATION, state="*")
async def location_handler(message: types.Message, state: FSMContext):
    nearest_restaurants = get_3_nearest_restaurants(message.location.latitude, message.location.longitude, 0)

    for restaurant in nearest_restaurants:
        image_id, text = restaurant.create_message_content(message.location.latitude, message.location.longitude)
        await message.answer_photo(photo=image_id, caption=text, reply_markup=create_open_map_kb(
            restaurant.latitude, restaurant.longitude, restaurant.name))

    await message.answer(text="<b>Больше заведений:</b>", reply_markup=create_show_more_kb())

    await state.update_data(state=1, user_latitude=message.location.latitude, user_longitude=message.location.longitude)