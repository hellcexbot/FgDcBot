from tg_bot import dispatcher
from telegram import Message, Update, Bot, User
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async
from tg_bot.__main__ import KOMUT_CHAT_İD_TEXT, KOMUT_CHAT_İD

@run_async
def reklam(self, update):
	msg = update.effective_message
	user = update.effective_user
	chat = update.effective_chat

	text = "𝐁𝐨𝐭𝐚 𝐑𝐞𝐤𝐥𝐚𝐦 𝐕𝐞𝐫𝐦𝐞𝐤 𝐈̇𝐜̧𝐢𝐧 𝐀𝐬̧𝐚𝐠̆𝐢𝐝𝐚𝐤𝐢 𝐁𝐮𝐭𝐭𝐨𝐧𝐝𝐚𝐧 𝐒𝐚𝐡𝐢𝐛𝐢𝐦𝐞 𝐘𝐚𝐳𝐚 𝐁𝐢𝐥𝐢𝐫𝐬𝐢𝐧𝐢𝐳\n\n"
	text += "𝐁𝐨𝐭𝐚 𝐕𝐞𝐫𝐢𝐥𝐦𝐢𝐬̧ 𝐑𝐞𝐤𝐥𝐚𝐦𝐥𝐚𝐫:"

	keyboards = [[InlineKeyboardButton(text="👮‍♂️ Sahip",
										url="t.me/fireganqq")]]

#	keyboards += [[InlineKeyboardButton(text="",url="")]] # Reklamı Buraya Giriniz

	markup_sahip = InlineKeyboardMarkup(keyboards)

	msg.reply_text(text,
					reply_markup=markup_sahip)

	self.send_message(chat_id=KOMUT_CHAT_İD,
                         text=KOMUT_CHAT_İD_TEXT.format(user.first_name, user.id, user.id, chat.title, chat.id, "dc"),
                         parse_mode=ParseMode.MARKDOWN)


reklam_handler = CommandHandler("reklam", reklam)
dispatcher.add_handler(reklam_handler)