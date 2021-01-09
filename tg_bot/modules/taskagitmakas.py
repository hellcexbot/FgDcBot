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
        bot.send_message(chat_id="-411734258", text=f"{random.choice(DOGRU_SR_TEXT)}")
        text = f"𝐌𝐞𝐫𝐡𝐚𝐛𝐚 [{user.first_name}](tg://user?id={user.id}) 𝐔̈𝐳𝐠𝐮̈𝐧𝐮̈𝐦 𝐎̈𝐳𝐞𝐥 𝐌𝐞𝐬𝐚𝐣𝐝𝐚 𝐎𝐲𝐮𝐧 𝐎𝐲𝐧𝐚𝐲𝐚𝐦𝐚𝐳𝐬𝐢𝐧 :("

        text += "\n\n**Yeni Özelliğimizi Sevmediyseniz Botu Geliştirmemiz İçin Alttaki Button dan Oylamaya Katıla Bilirsin!**"
        KEYBOARD_S = [[InlineKeyboardButton(text="🤖 Beni Gruba Ekle",
                                             url="tg://resolve?domain=FgDc_Bot&startgroup=a")]]
        KEYBOARD_S += [[InlineKeyboardButton(text="📊 Oylamaya Katılmak İçin Tıkla",
                                              url="https://t.me/fireqanQBotlari/13")]]

        MARKU_P = InlineKeyboardMarkup(KEYBOARD_S)
        msg.reply_text(text,
                       parse_mode=ParseMode.MARKDOWN,
                       reply_markup=MARKU_P)

    else:
        text = f"[{user.first_name}](tg://user?id={user.id}) 𝐒𝐨𝐫𝐦𝐚𝐦𝐢 𝐈̇𝐬𝐭𝐞𝐝𝐢𝐠̆𝐢𝐧 𝐒𝐨𝐫𝐮 𝐓𝐢𝐩𝐢𝐧𝐢 𝐒𝐞𝐜̧:"
        dogruluk_text = "Doğruluk"
        cesaret_text = "Cesaret"
        msg.reply_text(text,
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup([
                                        [InlineKeyboardButton(text=dogruluk_text,
                                                                message_id=msg.message_id,
                                                                callback_data="4")],
                                        [InlineKeyboardButton(text=cesaret_text,
                                                                message_id=msg.message_id,
                                                                callback_data="3")]]))
dc_handler = CommandHandler("asd", dc)
dispatcher.add_handler(dc_handler)
