import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dispatcher: Dispatcher):
    for admin in ADMINS:
        try:
            await dispatcher.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
