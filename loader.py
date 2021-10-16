from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from data import config
from data.restaurants import create_restaurants
from utils.amplitude import Amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


class Database:
    def __init__(self, restaurants):
        self.restaurants = restaurants

    def update_restaurants(self, restaurants):
        self.restaurants = restaurants


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

logging.info("Starting to parse restaurants.csv")
database = Database(create_restaurants())
logging.info("Parsing finished")

amplitude = Amplitude(config.AMPLITUDE_API_KEY)
