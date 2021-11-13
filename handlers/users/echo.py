import time

from aiogram import types, bot
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
    data = await state.get_data()
    suggest_state = data.get("suggest_state")

    if suggest_state == 1:
        await state.update_data(suggest_state=2, restaurant_name=message.text)
        await message.answer("Какие веганские позиции есть в этом заведении?")
    elif suggest_state == 2:
        await state.update_data(suggest_state=0)
        await message.answer("Мы проверим заведение и, возможно, добавим его в нашу базу. Спасибо!\n\nНам нужна помощь в заполнении базы мест. Если, вы хотите поучаствовать в развитии Vegan Map, напишите @oksnavau")

        restaurant_name = data.get("restaurant_name")
        await bot.send_message(config.ADMINS[0], f'#предложенное_заведение\n<b>{data.get("restaurant_name")}</b>\n{message.text}')
        await bot.send_message(config.ADMINS[1], f'#предложенное_заведение\n<b>{data.get("restaurant_name")}</b>\n{message.text}')
    else:
        await message.answer('''
        ⚠️ Если не работает кнопка (бывает с компьютера):
1. Нажмите на скрепку слева от поля ввода сообщения
2. Выберите «Геопозиция»
3. Отправить геопозицию (должен быть включен доступ Telegram к геопозиции)

🧭 Как проложить маршрут
1. Нажмите кнопку «Открыть карту» под сообщением с заведением
2. Тапните на сообщение с картой
3. Нажмите кнопку «Маршруты»
4. В меню выберите любимое приложение карт

🗺 Как посмотреть заведения в другом районе
1. Нажмите на скрепку слева от поля ввода сообщения
2. Выберите «Геопозиция»
3. Установите точку в интересующем месте

🚦 Статусы заведений
• 100% vegan: все позиции в заведении веганские
• Кухня – 100 vegan, по напиткам уточняйте: особый статус, который пришлось добавить для кафе «Огурцы» и «VeggieBox»
• Больше трёх веганских позиций: в заведении 4 и больше позиций по вегану
• Если блюд меньше трех, мы просто отображаем их список

❤️ Предложить заведение – /suggest

✉️ Вопросы и пожелания – @startsevdev''')

    logging.info("User {} sent other content".format(message.from_user.id))
    amplitude.log(message.from_user.id, "Other")

    # РАССЫЛКА
    # if message.text == "Ootro" and str(message.from_user.id) == config.ADMIN[0]:
    #     cluster = [[]]
    #     counter = 0
    #     with open('data/users.csv', newline='') as File:
    #         reader = csv.reader(File)
    #         for user_id in reader:
    #             if counter < 30:
    #                 cluster[len(cluster)-1].append(user_id[0])
    #                 counter += 1
    #             else:
    #                 counter = 0
    #                 cluster.append([])
    #     for c in cluster:
    #         for user_id in c:
    #             try:
    #                 await bot.send_message(user_id, "<b>Веганские завтраки в течение месяца</b>\n\nСегодня стартовал фестиваль Utroo\nhttps://t.me/utroo/1103\n\nИщите заведения фестиваля на нашей карте 📍\n\nВ фестивале участвуют 7 замечательных ресторанов («Мечтатели», Atlas bistro, Grecco, Tureckiy bistro, Merula на Невском, Bilbao и «Мойка 3»), а также петербургская сеть кондитерских «Британские пекарни» (а это 22 кафе по всему городу).\n\nЗавтраки без использования продуктов животного происхождения можно будет пробовать целый месяц. И речь – не о скучных кашах, но о необычных блюдах, в числе которых шоколадные панкейки с карамелью из комбучи, томаты со страчателлой из кешью, хашбраун из тыквы и веганский брауни!")
    #                 logging.info("Sent to " + user_id)
    #             except BaseException:
    #                 print("Ошибка про отправке сообщения рассылки")
    #         time.sleep(1.2)
    #     await message.answer("Рассылка отправлена")
    # else:
