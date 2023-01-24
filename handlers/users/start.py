from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.default.main_menu import menu_button
from utils.db_api.bot_users import create_bot_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    txt1 = f"<i>Dear</i> <b>{message.from_user.full_name},</b>"
    txt1 += "\nWelcome to the bot"
    txt1 += "\n\nWith this bot, you can convert your text to different fonts."
    await message.answer(text=txt1)
    txt2 = "<i>Please, select a font from the</i> <b>📋 Fonts list 📝 </b> <i>section, \
        \nor click</i> <b>☑️ Apply all fonts ✅</b><i> button to use all fonts at once</i>"
    await message.answer(text=txt2, reply_markup=menu_button)

    # User'ni database'ga saqlaymiz
    create_bot_user(message.from_user)
