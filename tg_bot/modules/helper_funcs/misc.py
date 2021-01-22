import html
import json
import random
from datetime import datetime
from typing import Optional, List


import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html

from tg_bot çar. Öfke nefrete yol açar. Nefret acıya yol açar. Korku içinde koşmaya devam edersen, yapabilirsin "
    "sonraki Vader ol.",
    "Birden fazla hesaplama yaptıktan sonra, saçmalıklarınıza olan ilgimin tam olarak 0 olduğuna karar verdim.",
    "Efsaneye göre, hala çalışıyorlar.",
    "Devam et, yine de seni burada istediğimizden emin değilim.",
    "Sen bir wizasın- Oh. Bekle. Sen Harry değilsin, devam et .",
    "SALONLARDA KOŞMAK YOK!",
    "Güle güle bebek.",
    "Köpekleri kim dışarı bıraktı?",
    "Komik çünkü kimsenin umurunda değil.",
    "Ah, ne yazık. Bunu beğendim.",
    "Açıkçası canım, umurumda değil.",
    "Milkshake'im bütün erkekleri bahçeye getiriyor... O yüzden daha hızlı koş!",
    "Gerçeği idare edemezsin!",
    "Uzun zaman önce, çok uzaktaki bir galakside ... Birisi bunu umursardı. Artık değil.",
    "Hey, şunlara bak! Kaçınılmaz banhammerden kaçıyorlar ... Sevimli.",
    "Önce Han vurdu. Ben de öyle.",
    "Neyin peşinden koşuyorsun, beyaz bir tavşan?",
    "Doktor'un dediği gibi... KOŞ!",
)      parse_mode=ParseMode.MARKDOWN)
    else:
        chat = update.effective_chat  # type: Optional[Chat]
        if chat.type == "private":
            update.effective_message.reply_text("Kimliğiniz: `{}`.".format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)

        else:
            update.effect
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(INFO_HANDLER)
dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)
dispatcher.add_handler(STATS_HANDLER)
dispatcher.add_handler(GDPR_HANDLER)
dispatcher.add_handler(STICKERID_HANDLER)
dispatcher.add_handler(GETSTICKER_HANDLER)
