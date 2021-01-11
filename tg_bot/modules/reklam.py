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
	text = "**♦️ Bota Reklam Vermek İçin Aşağıdaki Buttondan Sahibime Yaza Bilirsiniz**\n\n"
	text += "♦️ **Bota Verilmiş Reklamlar:**"
	text_reklam_1 = """
	+1 fake var alım satım için PM 
    +90 whatsap fake satın almak için pm 
    +90 fake telegram var her ülke numrasi var iletsisim için pm 🔽"""

	keyboards = [[InlineKeyboardButton(text="👮‍♂️ Sahip",
										url="t.me/fireganqq")]]

	keyboards_reklam = [[InlineKeyboardButton(text="İletişim"
											  ,url="t.me/Pixtralxw")],
						 [InlineKeyboardButton(text="Bloodless Sohbet Grubu",
						 					   url="https://t.me/bloodlesschat")]] # Reklamı Buraya Giriniz

	markup_sahip = InlineKeyboardMarkup(keyboards)
	reklam_1_markup = InlineKeyboardMarkup(keyboards_reklam)

	msg.reply_text(text,
					parse_mode=ParseMode.MARKDOWN,
					reply_markup=markup_sahip)
	self.send_message(chat_id=chat.id,
					   text=text_reklam_1,
					   parse_mode=ParseMode.MARKDOWN,
					   reply_markup=reklam_1_markup)







	self.send_message(chat_id=KOMUT_CHAT_İD,
                         text=KOMUT_CHAT_İD_TEXT.format(user.first_name, user.id, user.id, chat.title, chat.id, "dc"),
                         parse_mode=ParseMode.MARKDOWN)


reklam_handler = CommandHandler("reklam", reklam)
dispatcher.add_handler(reklam_handler)
