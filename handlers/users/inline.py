from aiogram import types

from loader import dispatcher


@dispatcher.callback_query_handler()
async def send_map(call: types.CallbackQuery):
    data = call.data.split(", ")
    await call.message.answer_location(float(data[0]), float(data[1]))
    await call.message.answer("<b>{}</b>".format(data[2]))
