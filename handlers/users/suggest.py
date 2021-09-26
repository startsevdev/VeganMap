from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandSuggest
import logging

from loader import dispatcher, amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.message_handler(CommandSuggest(), state="*")
async def bot_help(message: types.Message, state: FSMContext):
    await state.update_data(suggest_state=1)
    await message.answer("Отправьте сылку или навзание заведения")

    logging.info("User {} sent /help".format(message.from_user.id))
    amplitude.log(message.from_user.id, "/suggest")
