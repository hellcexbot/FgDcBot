import random, asyncio
from time import sleep

from tg_bot import dispatcher
from telegram import Message, Update, Bot, User
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async


@run_async
def tkm(bot, update):
    chat = update.effective_chat
    user = update.effective_user
    msg = update.effective_message  # type: Optional[Message]
    #SORU1 = msg.reply_text(random.choice(SORULAR_TEXT1))
    if chat.type == "private":
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
        text = f"[{user.first_name}](tg://user?id={user.id}) Birini Seç:"
        tas_text = "🥌 TAŞ"
        kagit_text = "📃 KAĞIT"
        makas_text = "✂️ MAKAS"

        msg.reply_text(text,
                        parse_mode=ParseMode.MARKDOWN,
                        reply_markup=InlineKeyboardMarkup([
                                        [InlineKeyboardButton(text=tas_text,
                                                                message_id=msg.message_id,
                                                                callback_data="tas_bttn")],
                                        [InlineKeyboardButton(text=kagit_text,
                                                                message_id=msg.message_id,
                                                                callback_data="kagit_bttn")],
                                        [InlineKeyboardButton(text=makas_text,
                                                                message_id=msg.message_id,
                                                                callback_data="makas_bttn")]]))
    query = update.callback_query
    msg_id = query.id
    msg = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    query.answer()


    if query.data == "tas_bttn":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐒𝐞𝐜̧𝐢𝐦 𝐘𝐚𝐩𝐭𝐢: 𝐓𝐚𝐬̧",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text="𝐁𝐨𝐭 𝐒𝐞𝐜̧𝐢𝐦 𝐘𝐚𝐩𝐢𝐲𝐨𝐫...")
        tkm_rndm = random.choice(["taş","kagı","makas"])
        if tkm_rndm == "taş":
            bot.send_message(chat_id=update.effective_chat.id,
                             text=f"𝐁𝐨𝐭 𝐒𝐞𝐜̧𝐢𝐦 𝐘𝐚𝐩𝐭𝐢: {tkm_rndm}",
                             parse_mode=ParseMode.MARKDOWN)
            bot.send_message(chat_id=update.effective_chat.id,
                             text="🤝 **BERABERE**",
                             parse_mode=ParseMode.MARKDOWN)
        else:
            bot.send_message(chat_id=update.effective_chat.id,
                             text=f": {tkm_rndm}",
                             parse_mode=ParseMode.MARKDOWN)
    if query.data == "2":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐈̇𝐜̧𝐢𝐧 𝐂𝐞𝐬𝐚𝐫𝐞𝐭 𝐒𝐨𝐫𝐮𝐬𝐮 𝐆𝐞𝐭𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫...",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(CESARET_SR_TEXT)}")

_handler = CommandHandler("tkm", tkm)
dispatcher.add_handler(_handler)
