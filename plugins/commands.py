import pyrogram
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup 
from translation import Translation 

@Client.on_message(Filters.text & Filters.private & Filters.incoming)
async def force(c, m):
      try:
        chat = await c.get_chat_member(-1001221642755, m.from_user.id)
        if chat.status=="kicked":
           await c.send_message(chat_id=m.chat.id, text="You are Banned 😝", reply_to_message_id=m.message_id)
           m.stop_propagation()
      except UserBannedInChannel:
         return await c.send_message(chat_id=m.chat.id, text="Hai you made a mistake so you are banned from channel so you are banned from me too 😜")
      except UserNotParticipant:
          button = [[InlineKeyboardButton('join Updates channel 🥰', url='https://t.me/Ns_bot_updates')]]
          markup = InlineKeyboardMarkup(button)
          return await c.send_message(chat_id=m.chat.id, text="""Hai bro,\n\n**You must join my channel for using me.**\n\nPress this button to join now 👇""", parse_mode='markdown', reply_markup=markup)
      m.continue_propagation()

@Client.on_message(Filters.command(["about"]) & Filters.private)
async def about(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤔 Help", callback_data="help")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.ABOUT,
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_message(Filters.command(["help"]) & Filters.private)
async def help(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤖 About", callback_data="about")], [InlineKeyboardButton("Add To Group", url="https://t.me/{}?startgroup=False".format(m.chat.username))]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_message(Filters.command(["start"]) & Filters.private)
async def start(c, m):
      button = [[InlineKeyboardButton("Creator 👨🏻‍💻", url="https://t.me/Ns_AnoNymouS"), InlineKeyboardButton("Add To channel 🔰", url="http://t.me/{}?startgroup=False".format(m.chat.username))], [InlineKeyboardButton("🤔 Help", callback_data="help"), InlineKeyboardButton("🤖 About", callback_data="about")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.START.format(m.from_user.first_name),
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)
