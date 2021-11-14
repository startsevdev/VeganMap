import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dispatcher, amplitude
from keyboards.default import send_geo


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('''
Привет!

Посмотрим, какие места есть рядом? Для этого нажмите «📍 Отправить геопозицию».
Если кнопка не работает, жмите /help
''', reply_markup=send_geo)

    logging.info("User {} sent /start".format(message.from_user.id))
    amplitude.log(message.from_user.id, "/start")
