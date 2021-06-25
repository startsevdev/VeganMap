from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dispatcher
from keyboards.default import send_geo


@dispatcher.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=send_geo)
