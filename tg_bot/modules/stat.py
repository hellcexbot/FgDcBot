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
♦️ Toplam Soru Sayısı: {T_SORU}
♦️ Doğruluk Soru Sayısı: {D_SORU}
♦️ Cesaret Soru Sayısı: {C_SORU}
♦️ Bot Versiyonu: {BOT_VERSİYON}

👮‍♂️ Soru, İstek Ve Öneri İçin Lütfen Sahibime Yazmakdan Çekinmeyin
"""

@run_async
def stat(bot, update):
	msg = update.effective_message.reply_text
	chat = update.effective_chat
	user = update.effective_user
	
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
