import random, asyncio
from time import sleep

from tg_bot.modules.helper_funcs.doguluksoru import DOGRU_SR_TEXT
from tg_bot.modules.helper_funcs.cesaretsoru import CESARET_SR_TEXT
from tg_bot.__main__ import KOMUT_CHAT_İD_TEXT, KOMUT_CHAT_İD
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
        text = f"‼️ **Merhaba [{user.first_name}](tg://user?id={user.id}) Üzgünüm Özel Mesajda Oyun Oynayamazsın :(**"

        text += "\n\n♦️ **Yeni Özelliğimizi Sevmediyseniz Botu Geliştirmemiz İçin Alttaki Button dan Oylamaya Katıla Bilirsin!**"
        KEYBOARD_S = [[InlineKeyboardButton(text="🤖 Beni Gruba Ekle",
                                             url="tg://resolve?domain=TRDogrulukCesaret_BOT&startgroup=a")]]
        KEYBOARD_S += [[InlineKeyboardButton(text="📊 Oylamaya Katılmak İçin Tıkla",
                                              url="https://t.me/fireqanQBotlari/13")]]

        MARKU_P = InlineKeyboardMarkup(KEYBOARD_S)
        msg.reply_text(text,
                       parse_mode=ParseMode.MARKDOWN,
                       reply_markup=MARKU_P)

    else:
        text = f"⭕️ [{user.first_name}](tg://user?id={user.id}) Sormamı İstediğin Soru Tipini Seç:"
        dogruluk_text = "Doğruluk"
        cesaret_text = "Cesaret"
        msg.reply_text(text,
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup([
                                        [InlineKeyboardButton(text=dogruluk_text,
                                                                message_id=msg.message_id,
                                                                callback_data="1")],
                                        [InlineKeyboardButton(text=cesaret_text,
                                                                message_id=msg.message_id,
                                                                callback_data="2")]]))
    bot.send_message(chat_id=KOMUT_CHAT_İD,
                         text=KOMUT_CHAT_İD_TEXT.format(user.first_name, user.id, user.id, chat.title, chat.id, "dc"),
                         parse_mode=ParseMode.MARKDOWN)
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
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"🛑 **[{user.first_name}](tg://user?id={user.id}) İçin Doğruluk Sorusu Getiriliyor...**",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(DOGRU_SR_TEXT)}")
    if query.data == "2":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"🛑 **[{user.first_name}](tg://user?id={user.id}) İçin Cesaret Sorusu Getiriliyor...**",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(CESARET_SR_TEXT)}")

dc_handler = CommandHandler("dc", dc)
dc_dc_handler = CallbackQueryHandler(button)
dispatcher.add_handler(dc_handler)
dispatcher.add_handler(dc_dc_handler)
