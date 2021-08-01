import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dispatcher
from keyboards.default import send_geo
from utils import amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("📍 Отправьте свою геопозицию. В ответ бот пришлёт три ближайшие заведения, где можно "
                         "полноценно поесть", reply_markup=send_geo)

    logging.info("User {} sent /start".format(message.from_user.id))
    amplitude.log_start_command(message.from_user.id)
