from config import Config
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from translation import Translation 

@Client.on_message(Filters.text & Filters.private & Filters.incoming)
async def force(c, m):
      try:
        chat = await c.get_chat_member(-1001221642755, m.from_user.id)
        if chat.status=="kicked":
           await c.send_message(chat_id=m.chat.id, text="You are Banned 😝", reply_to_message_id=m.message_id)
           m.stop_propagation()
      except UserNotParticipant:
          button = [[InlineKeyboardButton('join Updates channel 🥰', url='https://t.me/Ns_bot_updates')]]
          markup = InlineKeyboardMarkup(button)
          return await c.send_message(chat_id=m.chat.id, text="""Hai bro,\n\n**You must join my channel for using me.**\n\nPress this button to join now 👇""", parse_mode='markdown', reply_markup=markup)
      m.continue_propagation()

@Client.on_message(Filters.command("about") & Filters.private)
async def about(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤔 Help", callback_data="help")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.ABOUT,
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_message(Filters.command("help") & Filters.private)
async def help(c, m):
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤖 About", callback_data="about")], [InlineKeyboardButton("Add Me To Group 🔰", url="https://t.me/Postdeleter_NsBot?startgroup=False")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)

@Client.on_message(Filters.command("start") & Filters.private)
async def start(c, m):
      button = [[InlineKeyboardButton("Creator 👨🏻‍💻", url="https://t.me/Ns_AnoNymouS"), InlineKeyboardButton("Add Me To Group 🔰", url="http://t.me/Postdeleter_NsBot?startgroup=False")], [InlineKeyboardButton("🤔 Help", callback_data="help"), InlineKeyboardButton("🤖 About", callback_data="about")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.START.format(m.from_user.first_name),
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)
@Client.on_message(Filters.command(f"start@{Config.BOT.username}") & Filters.group)
async def start_group(c, m):
    bot = Config.BOT
    bot_permissions = await m.chat.get_member(bot.id)
    if not bot_permissions.can_delete_messages:
        await m.reply_text(
            text="Now give me the delete permission 🗑",
            quote=True
        )
    else:
        await m.reply_text(
            text="Yeah i am alive 🤩"
        )
