import pyrogram 
from pyrogram import Client, Filters 

@Client.on_message()
async def delete(c, m):
  if m.chat.type != "channel":
    if m.from_user.id is None:
       await m.delete()
    m.continue_propagation()
