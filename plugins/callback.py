import pyrogram
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup 
from translation import Translation

@Client.on_callback_query(Filters.create(lambda _, query: query.data.startswith('about')))          
async def about_cb(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤔 Help", callback_data="help")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.message.edit(text=Translation.ABOUT,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_callback_query(Filters.create(lambda _, query: query.data.startswith('help')))          
async def help_cb(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤖 About", callback_data="about")], [InlineKeyboardButton("Add Me To Group 🔰", url="https://t.me/Postdeleter_NsBot?startgroup=False")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.message.edit(text=Translation.HELP,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_callback_query(Filters.create(lambda _, query: query.data.startswith('close')))          
async def close_cb(c, m):
      await m.message.delete()
      await m.message.reply_to_message.delete()
