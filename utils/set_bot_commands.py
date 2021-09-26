from aiogram import types


async def set_default_commands(dispatcher):
    await dispatcher.bot.set_my_commands(
        [
            # types.BotCommand("start", "Запустить бота"),
            types.BotCommand("suggest", "Предложить заведение"),
            # types.BotCommand("help", "Помощь")
        ]
    )
