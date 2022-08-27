

from aiogram import types
from loader import dp

from keyboards.inline.callback_data import back_page, font_index, forward_page
from utils.FontsChanger import fonts_number, page_generator
from keyboards.inline.InlineKeyboards import generate_buttons
from data.Users import specific_font, all_fonts


@dp.callback_query_handler(forward_page.filter())
async def ForwardHandler(call: types.CallbackQuery, callback_data: dict):
    
    n = int(callback_data["index"])
    start = n+1
    end = n + 10

    # print(f"start = {start} \n end={end}\n")

    if end > fonts_number-1:
        end = fonts_number-1

    if start > fonts_number-1:
        await call.answer(text="You are already on the last page", cache_time=60)
    else:
        txt = page_generator(start, end)
        buttons = await generate_buttons(start, end)
        await call.message.edit_text(text=txt, reply_markup=buttons)
    await call.answer()


@dp.callback_query_handler(back_page.filter())
async def ForwardHandler(call: types.CallbackQuery, callback_data: dict):

    n = int(callback_data["index"])
    start = n-10
    end = n-1

    # print(f"start = {start} \n end={end}\n")

    if start < 1:
        await call.answer(text="You are already on the first page", cache_time=60)
    else:
        txt = page_generator(start, end)
        buttons = await generate_buttons(start, end)
        await call.message.edit_text(text=txt, reply_markup=buttons)
    await call.answer()


@dp.callback_query_handler(font_index.filter())
async def IndexHandler(call: types.CallbackQuery, callback_data: dict):
    n = int(callback_data["index"])

    specific_font[call.from_user.id] = n
    all_fonts[call.from_user.id] = False

    txt = "<b>Send me some text 🖋</b>"
    await call.message.answer(text=txt)
    await call.answer()

  




