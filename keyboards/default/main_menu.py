
from aiogram import types

menu_button = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(
                text="📋 Fonts list 📝"
            ),
            types.KeyboardButton(
                text="☑️ Apply all fonts ✅"
            ),
        ],
        [
            types.KeyboardButton(
                text="🤖 About Inline Mode 📃"
            ),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)