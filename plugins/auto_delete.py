import pyrogram 
from pyrogram import Client, Filters 

@Client.on_message(Filters.text)
async def delete(c, m):
    if m.from_user is None:
       await m.delete()
