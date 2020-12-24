import logging
logger = logging.getLogger(__name__)

import pyrogram 
from pyrogram import Client, Filters 


@Client.on_message(Filters.linked_channel)
async def delete(c, m):
    bot = await c.get_me()
    await m.chat.get_member(get_member)
    await m.delete()
