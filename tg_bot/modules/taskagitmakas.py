import random
from time import sleep

from tg_bot import dispatcher
from telegram import Message, Update, Bot, User
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

@run_async
def tkm(bot, update):
	msg = update.effective_message
	user = update.effective_user
	chat = update.effective_chat

	if chat.type == "private":
		text = f"𝐌𝐞𝐫𝐡𝐚𝐛𝐚 [{user.first_name}](tg://user?id={user.id}) 𝐔̈𝐳𝐠𝐮̈𝐧𝐮̈𝐦 𝐎̈𝐳𝐞𝐥 𝐌𝐞𝐬𝐚𝐣𝐝𝐚 𝐎𝐲𝐮𝐧 𝐎𝐲𝐧𝐚𝐲𝐚𝐦𝐚𝐳𝐬𝐢𝐧 :("

		KEYBOARD_S = [[InlineKeyboardButton(text="🤖 Beni Gruba Ekle",
                                            url="tg://resolve?domain=FgDc_Bot&startgroup=a")]]
		KEYBOARD_S += [[InlineKeyboardButton(text="📊 Oylamaya Katılmak İçin Tıkla",
                                              url="https://t.me/fireqanQBotlari/10")]]
		MARKU_P = InlineKeyboardMarkup(KEYBOARD_S)
		msg.reply_text(text, parse_mode=ParseMode.MARKDOWN, reply_markup=MARKU_P)
	else:
		TAS = "🥌 TAŞ"
		MAKAS = "✂️ MAKAS"
		KAGIT = "📃 KAĞIT"

		keyboards = [[InlineKeyboardButton(text=TAS,
											callback_data="3")]]

		keyboards += [[InlineKeyboardButton(text=KAGIT,
											callback_data="4")]]

		keyboards += [[InlineKeyboardButton(text=MAKAS,
											callback_data="5")]]

		markup  = InlineKeyboardMarkup(keyboards)

		msg.reply_text("[{user.first_name}](tg://user?id={user.id}) Birini Seç:",
						parse_mode=ParseMode.MARKDOWN,
						reply_markup=markup)


def tkm_button(bot, update):
    query = update.callback_query
    msg_id = query.id
    msg = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    query.answer()


    if query.data == "3":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐈̇𝐜̧𝐢𝐧 𝐃𝐨𝐠̆𝐫𝐮𝐥𝐮𝐤 𝐒𝐨𝐫𝐮𝐬𝐮 𝐆𝐞𝐭𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫...",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(DOGRU_SR_TEXT)}")
    if query.data == "4":
        bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)
        bot.send_message(chat_id=update.effective_chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐈̇𝐜̧𝐢𝐧 𝐂𝐞𝐬𝐚𝐫𝐞𝐭 𝐒𝐨𝐫𝐮𝐬𝐮 𝐆𝐞𝐭𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫...",
                         parse_mode=ParseMode.MARKDOWN)
        sleep(1)
        bot.send_message(chat_id=update.effective_chat.id, text=f"{random.choice(CESARET_SR_TEXT)}")


"""
def tkm_button(bot, update):
	query = update.callback_query
	msg = update.effective_message
	user = update.effective_user
	chat = update.effective_chat
	tkm = ["Taş", "Kağıt", "Makas"]
	tkm_random = random.choice(tkm)
	berabere = "🤝 **BERABERE**"
	win = f"✅ **[{user.first_name}](tg://user?id={user.id}) KAZANDI** 🥳"
	bot_win = "❌ **BOT KAZANDI**"

	query.answer()

	if query.data == "3":
		bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)

		bot.send_message(chat_id=chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐓𝐚𝐬̧ 𝐒𝐞𝐜̧𝐞𝐧𝐞𝐠̆𝐢𝐧𝐢 𝐒𝐞𝐜̧𝐭𝐢...",
                         parse_mode=ParseMode.MARKDOWN)
		bot.send_message(chat_id=chat.id,
						  text="**Bot Seçim Yapıyor...**",
						  parse_mode=ParseMode.MARKDOWN)

		if tkm_random == "Taş":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{berabere}",
							 parse_mode=ParseMode.MARKDOWN)

		elif tkm_random == "Kağıt":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{bot_win}",
							 parse_mode=ParseMode.MARKDOWN)
			

		elif tkm_random == "Makas":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{win}",
							 parse_mode=ParseMode.MARKDOWN)

	if query.data == "4":
		bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)

		bot.send_message(chat_id=chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐊𝐚𝐠𝐢𝐭 𝐒𝐞𝐜̧𝐞𝐧𝐞𝐠̆𝐢𝐧𝐢 𝐒𝐞𝐜̧𝐭𝐢...",
                         parse_mode=ParseMode.MARKDOWN)
		bot.send_message(chat_id=chat.id,
						  text="**Bot Seçim Yapıyor...**",
						  parse_mode=ParseMode.MARKDOWN)

		if tkm_random == "Taş":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{win}",
							 parse_mode=ParseMode.MARKDOWN)

		elif tkm_random == "Kağıt":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{berabere}",
							 parse_mode=ParseMode.MARKDOWN)
			

		elif tkm_random == "Makas":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{bot_win}",
							 parse_mode=ParseMode.MARKDOWN)
	
	if query.data == "5":
		bot.delete_message(chat_id=chat.id,
                           message_id=msg.message_id)

		bot.send_message(chat_id=chat.id,
                         text=f"[{user.first_name}](tg://user?id={user.id}) 𝐌𝐚𝐤𝐚𝐬 𝐒𝐞𝐜̧𝐞𝐧𝐞𝐠̆𝐢𝐧𝐢 𝐒𝐞𝐜̧𝐭𝐢...",
                         parse_mode=ParseMode.MARKDOWN)
		bot.send_message(chat_id=chat.id,
						  text="**Bot Seçim Yapıyor...**",
						  parse_mode=ParseMode.MARKDOWN)

		if tkm_random == "Taş":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{bot_win}",
							 parse_mode=ParseMode.MARKDOWN)

		elif tkm_random == "Kağıt":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{win}",
							 parse_mode=ParseMode.MARKDOWN)
			

		elif tkm_random == "Makas":
			sleep(120)
			bot.send_message(chat_id=chat.id,
							 text=f"Bot Seçim Yaptı: {tkm_random}")
			sleep(30)
			bot.send_message(chat_id=chat.id,
							 text=f"{berabere}",
							 parse_mode=ParseMode.MARKDOWN)
"""
dc_handler = CommandHandler("tkm", tkm)
dc_dc_handler = CallbackQueryHandler(tkm_button)
dispatcher.add_handler(dc_handler)
dispatcher.add_handler(dc_dc_handler)
