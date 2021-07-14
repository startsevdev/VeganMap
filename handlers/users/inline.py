from aiogram import types


from loader import dispatcher


@dispatcher.callback_query_handler(text_contains='open_map')
async def send_map(call: types.CallbackQuery):
    data = call.data.split(":")
    await call.message.answer_location(float(data[1]), float(data[2]))
    await call.message.answer("<b>{}</b>".format(data[3]))


@dispatcher.callback_query_handler(text_contains='show_more')
async def show_more(call: types.CallbackQuery):
    data = call.data.split(":")
    await call.message.answer("SHOW MORE")
    await call.message.answer(data[1]+data[2])
