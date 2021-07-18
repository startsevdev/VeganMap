from aiogram import types

from loader import dispatcher
from data.config import ADMINS


@dispatcher.message_handler(content_types=types.ContentTypes.PHOTO, user_id=ADMINS)
async def location_handler(message: types.Message):
    photo_id = message.photo[0].file_id
    await message.answer(photo_id)
