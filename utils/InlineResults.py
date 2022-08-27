
from utils.FontsChanger import fonts_lst, fonts_number, compare_dict

from aiogram import types

import uuid


async def inline_results(matn):
    matnchalar = []
    extra = []

    n  = 50 if fonts_number > 50 else fonts_number


    for k in range(n):
        matnchalar.append("")
        extra.append(len(fonts_lst[k])//62)


    for i in matn:
        index = compare_dict.get(i)
        if index != None:
            for l in range(n):
                matnchalar[l] += fonts_lst[l][index*extra[l]:(index+1)*extra[l]]
        else:
            for l in range(n):
                matnchalar[l] += i
    
    results = []
    
    for j in matnchalar:
        results.append(
            types.InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=j,
                input_message_content=types.InputTextMessageContent(
                    message_text=j,
                ),
                description="Font changer"
            ),
        )
    return results
