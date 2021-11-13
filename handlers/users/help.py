from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher import FSMContext

import logging

from loader import dispatcher, amplitude


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


@dispatcher.message_handler(CommandHelp())
async def bot_help(message: types.Message, state: FSMContext):
    text = ('''   
⚠️ Если не работает кнопка (бывает с компьютера):
1. Нажмите на скрепку слева от поля ввода сообщения
2. Выберите «Геопозиция»
3. Отправить геопозицию (должен быть включен доступ Telegram к геопозиции)

🧭 Проложить маршрут
1. Нажмите кнопку «Открыть карту» под сообщением с заведением
2. Тапните на сообщение с картой
3. Нажмите кнопку «Маршруты»
4. В меню выберите любимое приложение карт

🗺 Посмотреть заведения в другом районе
1. Нажмите на скрепку слева от поля ввода сообщения
2. Выберите «Геопозиция»
3. Установите точку в интересующем месте

🚦 Статусы заведений
• 100% vegan: все позиции в заведении веганские
• Кухня – 100 vegan, по напиткам уточняйте: особый статус, который пришлось добавить для кафе «Огурцы» и «VeggieBox»
• Больше трёх веганских позиций: в заведении 4 и больше позиций по вегану
• Если блюд меньше трех, мы просто отображаем их список

❤️ Предложить заведение – /suggest

✉️ Вопросы и пожелания – @startsevdev
    ''')
    await message.answer(text)

    # ДЛЯ КЕЙСА, КОГДА ПЕРЕД ЭТИМ НЕ ЗАКОНЧИЛ ПРЕДЛОЖЕНИЕ ЗАВЕДЕНИЯ
    async with state.proxy() as data:
        data["suggest_state"] = 0

    logging.info("User {} sent /help".format(message.from_user.id))
    amplitude.log(message.from_user.id, "/help")
