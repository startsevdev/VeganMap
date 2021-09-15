import time

from aiogram import types
from aiogram.dispatcher import FSMContext
import csv
import logging

from loader import dispatcher, amplitude, bot
from data import config


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dispatcher.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    if message.text == "Ootro" and str(message.from_user.id) == config.ADMIN[0]:
        cluster = [[]]
        counter = 0
        with open('data/users.csv', newline='') as File:
            reader = csv.reader(File)
            for user_id in reader:
                if counter < 30:
                    cluster[len(cluster)-1].append(user_id[0])
                    counter += 1
                else:
                    counter = 0
                    cluster.append([])
        for c in cluster:
            for user_id in c:
                try:
                    await bot.send_message(user_id, "<b>Веганские завтраки в течение месяца</b>\n\nСегодня стартовал фестиваль Utroo\nhttps://t.me/utroo/1103\n\nИщите заведения фестиваля на нашей карте 📍\n\nВ фестивале участвуют 7 замечательных ресторанов («Мечтатели», Atlas bistro, Grecco, Tureckiy bistro, Merula на Невском, Bilbao и «Мойка 3»), а также петербургская сеть кондитерских «Британские пекарни» (а это 22 кафе по всему городу).\n\nЗавтраки без использования продуктов животного происхождения можно будет пробовать целый месяц. И речь – не о скучных кашах, но о необычных блюдах, в числе которых шоколадные панкейки с карамелью из комбучи, томаты со страчателлой из кешью, хашбраун из тыквы и веганский брауни!")
                    logging.info("Sent to " + user_id)
                except BaseException:
                    print("Ошибка про отправке сообщения рассылки")
            time.sleep(1.2)
        await message.answer("Рассылка отправлена")
    else:
        await message.answer("📍 Отправьте свою геопозицию. В ответ мы пришлем три ближайшие места\n")

    logging.info("User {} sent other content".format(message.from_user.id))
    amplitude.log(message.from_user.id, "Other")
