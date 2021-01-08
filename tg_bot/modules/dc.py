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
        text = f"𝐌𝐞𝐫𝐡𝐚𝐛𝐚 {first_name} 𝐔̈𝐳𝐠𝐮̈𝐧𝐮̈𝐦 𝐎̈𝐳𝐞𝐥 𝐌𝐞𝐬𝐚𝐣𝐝𝐚 𝐎𝐲𝐮𝐧 𝐎𝐲𝐧𝐚𝐲𝐚𝐦𝐚𝐳𝐬𝐢𝐧 :("

        KEYBOARD_S = [[InlineKeyboardButton(text="🤖 Beni Gruba Ekle",
                                            url="tg://resolve?domain=FgDc_Bot&startgroup=a")]]

        MARKU_P = InlineKeyboardMarkup(KEYBOARD_S)
        msg.reply_text(text,
                       reply_markup=MARKU_P)

    else:
        text = f"[{user.first_name}](tg://user?id={user.id}) \n**Selam**𝐒𝐨𝐫𝐦𝐚𝐦𝐢 𝐈̇𝐬𝐭𝐞𝐝𝐢𝐠̆𝐢𝐧 𝐒𝐨𝐫𝐮 𝐓𝐢𝐩𝐢𝐧𝐢 𝐒𝐞𝐜̧:"
        dogruluk_text = "Doğruluk"
        cesaret_text = "Cesaret"
        msg.reply_text(text,
                        parse_mode=ParseMode.MarkDown,
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
        bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name} 𝐈̇𝐜̧𝐢𝐧 𝐃𝐨𝐠̆𝐫𝐮𝐥𝐮𝐤 𝐒𝐨𝐫𝐮𝐬𝐮 𝐆𝐞𝐭𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫...")
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(DOGRU_SR_TEXT)}")
    if query.data == "2":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{user.first_name} 𝐈̇𝐜̧𝐢𝐧 𝐂𝐞𝐬𝐚𝐫𝐞𝐭 𝐒𝐨𝐫𝐮𝐬𝐮 𝐆𝐞𝐭𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫...")
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(CESARET_SR_TEXT)}")

dc_handler = CommandHandler("dc", dc)
dc_dc_handler = CallbackQueryHandler(button)
dispatcher.add_handler(dc_handler)
dispatcher.add_handler(dc_dc_handler)
