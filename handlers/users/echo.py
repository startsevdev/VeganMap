from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dispatcher


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dispatcher.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer("📍 Отправьте свою геопозицию. В ответ мы пришлем три ближайшие заведения.\n")

# # Эхо хендлер, куда летят текстовые сообщения без указанного состояния
# @dispatcher.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(f"Эхо без состояния."
#                          f"Сообщение:\n"
#                          f"{message.text}")
#     await message.answer_photo(message.text)
#
#
# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dispatcher.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
