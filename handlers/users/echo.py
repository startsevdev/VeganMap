from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dispatcher, amplitude
import logging


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dispatcher.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer("📍 Отправьте свою геопозицию. В ответ мы пришлем три ближайшие места\n")

    logging.info("User {} sent other content".format(message.from_user.id))
    amplitude.log(message.from_user.id, "Other")
