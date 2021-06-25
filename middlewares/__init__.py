from aiogram import Dispatcher

from loader import dispatcher
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dispatcher.middleware.setup(ThrottlingMiddleware())
