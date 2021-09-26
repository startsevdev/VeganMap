import logging
from aiogram import types

from loader import dispatcher, amplitude, restaurants
from aiogram.dispatcher import FSMContext
from data.restaurants import Restaurant

from utils.get_nearest_restaurants import get_nearest_restaurant_id
from keyboards.inline.restaurant_kb import create_restaurant_kb
from keyboards.inline.send_next_kb import create_send_next_kb


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.callback_query_handler(text_contains='send_map')
async def send_map(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    r_id = int(call.data.split(":")[1])
    restaurant: Restaurant = restaurants[r_id]
    await call.message.answer_location(restaurant.latitude, restaurant.longitude)
    await call.message.answer(f"<b>{restaurant.name}</b>", reply_markup=create_send_next_kb())

    # ДЛЯ КЕЙСА, КОГДА ПЕРЕД ЭТИМ НЕ ЗАКОНЧИЛ ПРЕДЛОЖЕНИЕ ЗАВЕДЕНИЯ
    async with state.proxy() as data:
        data["suggest_state"] = 0

    logging.info(f'User {call.from_user.id} clicked "Open map" under {restaurant.name}')
    amplitude.log(call.from_user.id, "Open map")


@dispatcher.callback_query_handler(text_contains='send_next')
async def send_next(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    user_latitude, user_longitude, user_state = data.get("user_latitude"), data.get("user_longitude"), data.get("state")

    try:
        key = get_nearest_restaurant_id(user_latitude, user_longitude, user_state)
    except TypeError:
        await call.message.answer("😞 У нас что-то пошло не так. Пожалуйста, отправьте геопозицию повторно")
    except IndexError:
        await call.message.answer("🏁 Вы долистали до конца. Чтобы начать новый поиск, отправьте геопозицию")
    else:
        image_id, text = restaurants[key].create_message_content(user_latitude, user_longitude)
        await call.message.answer_photo(photo="AgACAgIAAxkBAAIHQ2FQeaWAJNuVOT69C7ZidkrcRZVYAALFtTEbp1aJSqPtScWJ3G5fAQADAgADcwADIQQ", caption=text, reply_markup=create_restaurant_kb(key))
        async with state.proxy() as data:
            data["state"] += 1
            # ДЛЯ КЕЙСА, КОГДА ПЕРЕД ЭТИМ НЕ ЗАКОНЧИЛ ПРЕДЛОЖЕНИЕ ЗАВЕДЕНИЯ
            data["suggest_state"] = 0

    logging.info("User {} clicked inline button «Show more»".format(call.from_user.id))
    amplitude.log(call.from_user.id, "Next")

