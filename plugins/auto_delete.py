import logging
logger = logging.getLogger(__name__)

import pyrogram 
from pyrogram import Client, filters 


@Client.on_message(filters.linked_channel & filters.group)
async def delete(c, m):
    bot = await c.get_me()
    bot_permissions = await m.chat.get_member(bot.id)
    if not bot_permissions.can_delete_messages:
        return await m.reply_text("I don't have sufficient rights to delete the files, So please give me right to delete")
    await m.delete()
