import random, asyncio
from time import sleep

from tg_bot.modules.helper_funcs.doguluksoru import DOGRU_SR_TEXT
from tg_bot.modules.helper_funcs.cesaretsoru import CESARET_SR_TEXT
from tg_bot import dispatcher
from telegram import Message, Update, Bot, User
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async


@run_async
def dc(bot, update):
    chat = update.effective_chat
    user = update.effective_user
    msg = update.effective_message

    bot.send_message(chat_id=chat.id,
                     text=f"{chat.id}",
                     parse_mode=ParseMode.MARKDOWN)

dc_handler = CommandHandler("id", dc)
dispatcher.add_handler(dc_handler)
