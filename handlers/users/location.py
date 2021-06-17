from aiogram import types

from loader import dp


# Сюда летят сообщения с ЛОКАЦИЕЙ
@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    await message.answer("Ваши координаты: {0}, {1}".format(message.location.latitude, message.location.longitude))
    await message.answer((get_address(message.location)))
