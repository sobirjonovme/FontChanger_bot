

from aiogram import types
from keyboards.inline import callback_data
from keyboards.inline.callback_data import font_index, forward_page, back_page

async def generate_buttons(start, end):
    buttons = []
    if end-start > 4:
        buttons += [[], []] 
        for i in range(start, start+5):
            buttons[0].append(
                types.InlineKeyboardButton(
                        text=i,
                        callback_data=font_index.new(index=i)
                    )
            )
        for j in range(i+1, end+1):
            buttons[1].append(
                types.InlineKeyboardButton(
                        text=j,
                        callback_data=font_index.new(index=j)
                    )
            )
    else:
        buttons.append([])
        for i in range(start, end+1):
            buttons[0].append(
                types.InlineKeyboardButton(
                        text=i,
                        callback_data=font_index.new(index=i)
                    )
            )

    buttons.append(
        [
            types.InlineKeyboardButton(
                text="⬅️",
                callback_data=back_page.new(index=start)
            ),
            types.InlineKeyboardButton(
                text="➡️",
                callback_data=forward_page.new(index=end)
            ),
        ]
    )
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
    
            
