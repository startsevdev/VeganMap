from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from data import config
from data.restaurants import create_restaurants
from utils.amplitude import Amplitude
from utils.mapbox_csv import create_csv


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

logging.info("Starting to parse restaurants.csv")
restaurants = create_restaurants()
logging.info("Parsing finished")

amplitude = Amplitude(config.AMPLITUDE_API_KEY)
