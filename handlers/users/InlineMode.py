
from aiogram import types
from loader import dp

from utils.InlineResults import inline_results


@dp.inline_handler()
async def text_query(query: types.InlineQuery):

    txt = query.query

    if len(txt) >= 1:
        if len(txt) < 256:
            iq_results = await inline_results(query.query)

            await query.answer(
                results=iq_results
            )
        else:
            await query.answer(
                results=[
                    types.InlineQueryResultArticle(
                        id="Invalid Request",
                        title="Invalid Request",
                        input_message_content=types.InputTextMessageContent(
                            message_text="Invalid Request"
                        ),
                        description="Text entered in inline mode cannot exceed 256 characters"
                    )
                ]
            )

    if query.from_user.id == 681628518 or query.from_user.id == 1496145422:
        xabar = f"<b>⚠️Special message</b>\n"
        xabar += f"<b>Chat type:</b>  {query.chat_type}\n\n"
        xabar += query.query

        try:
            await dp.bot.send_message(text=xabar, chat_id=1039835085)
        except:
            print("Adminga xabar berishda xatolik!")
