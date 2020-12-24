import logging
logger = logging.getLogger(__name__)

import pyrogram 
from pyrogram import Client, Filters 


@Client.on_message(Filters.linked_channel)
async def delete(c, m):
    bot = await c.get_me()
    bot_details = await m.chat.get_member(bot.id)
    print(bot_details)
    await m.delete()
