from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from data.restaurants import create_restaurants

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
restaurants = create_restaurants()
print(restaurants[0].name)
