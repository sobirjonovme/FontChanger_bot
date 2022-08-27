
from aiogram import types

menu_button = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(
                text="📋 Shriftlar ro'yxati 📝"
            ),
            types.KeyboardButton(
                text="☑️ Barcha shriftlarni qo'llash ✅"
            ),
        ],
        [
            types.KeyboardButton(
                text="🤖  Inline Mode haqida  📃"
            ),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)