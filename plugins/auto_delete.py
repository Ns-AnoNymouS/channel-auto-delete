import logging
logger = logging.getLogger(__name__)

import pyrogram 
from pyrogram import Client, Filters 


@Client.on_message(Filters.linked_channel)
async def delete(c, m):
    bot = await c.get_me()
    print(bot)
    await m.delete()
