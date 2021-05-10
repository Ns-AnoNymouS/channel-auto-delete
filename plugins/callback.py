import pyrogram
from pyrogram import Client, filters as Filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from translation import Translation

@Client.on_callback_query(Filters.regex('^about$'))       
async def about_cb(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤔 Help", callback_data="help")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.message.edit(text=Translation.ABOUT,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_callback_query(Filters.regex('^help$'))         
async def help_cb(c, m):
      bot = await c.get_me()
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤖 About", callback_data="about")], [InlineKeyboardButton("Add Me To Group 🔰", url=f"https://t.me/{bot.username}?startgroup=False")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.message.edit(text=Translation.HELP,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_callback_query(Filters.regex('^close$'))          
async def close_cb(c, m):
      await m.message.delete()
      await m.message.reply_to_message.delete()
