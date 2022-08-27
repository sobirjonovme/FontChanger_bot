from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from keyboards.default.main_menu import menu_button


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    txt1 = f"<i>Assalom-u alaykum</i>, <b>{message.from_user.full_name}</b>"
    txt1 += "\nBotimizga xush kelibsiz!"
    txt1 += "\n\nBu bot orqali siz yuborgan matningizni turli shriftlarga o'tkazishingiz mumkin."
    await message.answer(text=txt1)
    txt2 = "<i>Iltimos,</i> <b>📋 Shriftlar ro'yxati 📝 </b>"
    txt2 += "<i>bo'limi orqali biror shriftni tanlang,</i>"
    txt2 += "<i> yoki birdaniga barcha shriftlardan foydalanish uchun</i>"
    txt2 +=  " <b>☑️ Barcha shriftlarni qo'llash ✅</b><i> tugmasini bosing</i>"
    await message.answer(text=txt2, reply_markup=menu_button)

