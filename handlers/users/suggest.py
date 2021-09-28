from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
import logging

from loader import dispatcher, amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


class CommandSuggest(Command):
    """
    This filter based on :obj:`Command` filter but can handle only ``/suggest`` command.
    """

    def __init__(self):
        super().__init__(['suggest'])


@dispatcher.message_handler(CommandSuggest(), state="*")
async def bot_help(message: types.Message, state: FSMContext):
    await state.update_data(suggest_state=1)
    await message.answer("Отправьте сылку или навзание заведения")

    logging.info("User {} sent /suggest".format(message.from_user.id))
    amplitude.log(message.from_user.id, "/suggest")
