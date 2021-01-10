from tg_bot.modules.helper_funcs.doguluksoru import DOGRU_SR_TEXT
from tg_bot.modules.helper_funcs.cesaretsoru import CESARET_SR_TEXT
from tg_bot import dispatcher
from tg_bot.__main__ import BOT_VERSİYON
from telegram import Message, Update, Bot, User
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async
from tg_bot.__main__ import KOMUT_CHAT_İD_TEXT, KOMUT_CHAT_İD

D_SORU = len(DOGRU_SR_TEXT)
C_SORU = len(CESARET_SR_TEXT)
T_SORU = D_SORU + C_SORU

TEXT_MSG = f"""
♦️ 𝑻𝒐𝒑𝒍𝒂𝒎 𝑺𝒐𝒓𝒖 𝑺𝒂𝒚ı𝒔ı: {T_SORU}
♦️ 𝘿𝙤𝙜𝙧𝙪𝙡𝙪𝙠 𝙎𝙤𝙧𝙪 𝙎𝙖𝙮ı𝙨ı: {D_SORU}
♦️ 𝘾𝙚𝙨𝙖𝙧𝙚𝙩 𝙎𝙤𝙧𝙪 𝙎𝙖𝙮ı𝙨ı: {C_SORU}
♦️ 𝘽𝙤𝙩 𝙑𝙚𝙧𝙨𝙞𝙮𝙤𝙣𝙪: {BOT_VERSİYON}

👮‍♂️ 𝙎𝙤𝙧𝙪, 𝙄𝙨𝙩𝙚𝙠 𝙑𝙚 𝙊𝙣𝙚𝙧𝙞 𝙄𝙘𝙞𝙣 𝙇𝙪𝙩𝙛𝙚𝙣 𝙎𝙖𝙝𝙞𝙗𝙞𝙢𝙚 𝙔𝙖𝙯𝙢𝙖𝙠𝙙𝙖𝙣 𝙆𝙖𝙘𝙞𝙣𝙢𝙖
"""

@run_async
def stat(bot, update):
	msg = update.effective_message.reply_text

	keyboards = [[InlineKeyboardButton(text="👮‍♂️ Sahibim",
									   url="t.me/fireganqq")]]

	markup = InlineKeyboardMarkup(keyboards)

	msg(text=TEXT_MSG,
		reply_markup=markup)

	bot.send_message(chat_id=KOMUT_CHAT_İD,
                         text=KOMUT_CHAT_İD_TEXT.format(user.first_name, user.id, user.id, chat.title, chat.id, "stat"),
                         parse_mode=ParseMode.MARKDOWN)

stat_handler = CommandHandler("stat", stat)
dispatcher.add_handler(stat_handler)
