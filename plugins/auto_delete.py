import pyrogram 
from pyrogram import Client, Filters 

@Client.on_message(Filters.linked_channel)
async def delete(c, m):
    await m.delete()
