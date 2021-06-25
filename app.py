from aiogram import executor

from loader import dispatcher
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    # Устанавливаем дефолтные команды
    await set_default_commands(dp)

    # Уведомляет про запуск
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=on_startup)
