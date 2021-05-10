from config import Config
from pyrogram import Client, filters as Filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from translation import Translation 


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
      bot = await c.get_me()
      button = [[InlineKeyboardButton("⛔ Close", callback_data="close"), InlineKeyboardButton("🤖 About", callback_data="about")], [InlineKeyboardButton("Add Me To Group 🔰", url=f"https://t.me/{bot.username}?startgroup=False")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)


@Client.on_message(Filters.command("start") & Filters.private)
async def start(c, m):
      bot = await c.get_me()
      button = [[InlineKeyboardButton("Creator 👨🏻‍💻", url="https://t.me/Ns_AnoNymouS"), InlineKeyboardButton("Add Me To Group 🔰", url=f"http://t.me/{bot.username}?startgroup=False")], [InlineKeyboardButton("🤔 Help", callback_data="help"), InlineKeyboardButton("🤖 About", callback_data="about")]]
      reply_markup = InlineKeyboardMarkup(button)
      await m.reply_text(text=Translation.START.format(m.from_user.first_name),
                         reply_to_message_id=m.message_id,
                         reply_markup=reply_markup,
                         disable_web_page_preview=True)


@Client.on_message(Filters.command(f"start{Config.BOT_USERNAME}") & Filters.group)
async def start_group(c, m):
    bot = await c.get_me()
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
