from tg_bot import dispatcher
from telegram import Message, Update, Bot, User
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext.dispatcher import run_async
from tg_bot.__main__ import KOMUT_CHAT_İD_TEXT, KOMUT_CHAT_İD

@run_async
def banket(bot, update):
	msg = update.effective_message.reply_text
	user = update.effective_user
	chat = update.effective_chat

	keyboards = [[InlineKeyboardButton(text="📊 Anket 1",
										url="https://t.me/fireqanQBotlari/13")]]

	keyboards += [[InlineKeyboardButton(text="📊 Anket 2",
										url="https://t.me/fireqanQBotlari/14")]]

	markup = InlineKeyboardMarkup(keyboards)

	msg("⭕️ Aktif Botla İlgili Anketler 🔽",
		 reply_markup=markup)

	bot.send_message(chat_id=KOMUT_CHAT_İD,
                         text=KOMUT_CHAT_İD_TEXT.format(user.first_name, user.id, user.id, chat.title, chat.id, "stat"),
                         parse_mode=ParseMode.MARKDOWN)

banket_handler = CommandHandler("banket", banket)
dispatcher.add_handler(banket_handler)
