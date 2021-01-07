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
    msg = update.effective_message  # type: Optional[Message]
    #SORU1 = msg.reply_text(random.choice(SORULAR_TEXT1))
    if chat.type == "private":
        first_name = update.effective_user.first_name
        text = f"{first_name} Sormamı İstediğin Soru Tipini Seç:"
        dogruluk_text = "Doğruluk"
        cesaret_text = "Cesaret"
        msg.reply_text(text,
                        reply_markup=InlineKeyboardMarkup([
                                        [InlineKeyboardButton(text=dogruluk_text,
                                                                message_id=msg.message_id,
                                                                callback_data="1")],
                                        [InlineKeyboardButton(text=cesaret_text,
                                                                message_id=msg.message_id,
                                                                callback_data="2")]]))
    else:
        text = f"{user.first_name} Sormamı İstediğin Soru Tipini Seç:"
        dogruluk_text = "Doğruluk"
        cesaret_text = "Cesaret"
        msg.reply_text(text,
                        reply_markup=InlineKeyboardMarkup([
                                        [InlineKeyboardButton(text=dogruluk_text,
                                                                message_id=msg.message_id,
                                                                callback_data="1")],
                                        [InlineKeyboardButton(text=cesaret_text,
                                                                message_id=msg.message_id,
                                                                callback_data="2")]]))
def button(bot, update):
    query = update.callback_query
    msg_id = query.id
    msg = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    query.answer()


    if query.data == "1":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        msg.reply_text(text=f"{user.first_name} İçin Doğruluk Sorusu Getiriliyor...")
        sleep(2.5)
        msg.reply_text(text=f"{random.choice(DOGRU_SR_TEXT)}")
    if query.data == "2":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name} İçin Cesaret Sorusu Getiriliyor...")
        sleep(2.5)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(CESARET_SR_TEXT)}")

dc_handler = CommandHandler("dc", dc)
dc_dc_handler = CallbackQueryHandler(button)
dispatcher.add_handler(dc_handler)
dispatcher.add_handler(dc_dc_handler)
