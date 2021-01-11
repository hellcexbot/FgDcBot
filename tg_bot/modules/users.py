from io import BytesIO
from time import sleep
from typing import Optional

from telegram import TelegramError, Chat, Message, ParseMode
from telegram import Update, Bot
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async

import tg_bot.modules.sql.users_sql as sql
from tg_bot import dispatcher

USERS_GROUP = 4


@run_async
def broadcast(bot: Bot, update: Update):
    to_send = update.effective_message.text.split(None, 1)
    if len(to_send) >= 1:
        chats = sql.get_all_chats() or []
        failed = 0
        for chat in chats:
            try:
                bot.sendMessage(int(chat.chat_id), to_send[1])
                sleep(0)
            except TelegramError:
                failed += 1
                
        update.effective_message.reply_text("Yayın tamamlandı. {} grup mesajı alamadı, muhtemelen "
                                            "tekmelenme nedeniyle.".format(failed))


@run_async
def log_user(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    msg = update.effective_message  # type: Optional[Message]

    sql.update_user(msg.from_user.id,
                    msg.from_user.username,
                    chat.id,
                    chat.title)

    if msg.reply_to_message:
        sql.update_user(msg.reply_to_message.from_user.id,
                        msg.reply_to_message.from_user.username,
                        chat.id,
                        chat.title)

    if msg.forward_from:
        sql.update_user(msg.forward_from.id,
                        msg.forward_from.username)



@run_async
def chats(bot: Bot, update: Update):
    all_chats = sql.get_all_chats() or []
    chatfile = 'Kullanıcı listesi:\n\n'
    for chat in all_chats:
        chatfile += "{} - ({})\n".format(chat.chat_name, chat.chat_id)

    with BytesIO(str.encode(chatfile)) as output:
        output.name = "chatlist.txt"
        update.effective_message.reply_document(document=output, filename="chatlist.txt",
                                                caption="Veritabanımdaki sohbetlerin listesi burada.")

@run_async
def pms(bot: Bot, update: Update):
    all_pms = sql.get_all_pms() or []
    pmfile = 'Kullanıcı listesi:\n\n'
    for pm in all_pms:
        pmfile += "{} - ({})\n".format(pm.username, pm.user_id)

    with BytesIO(str.encode(pmfile)) as output:
        output.name = "pmlist.txt"
        update.effective_message.reply_document(document=output, filename="pmlist.txt",
                                                caption="Veritabanımdaki kullanıcıların listesi burada.")

def __stats__():
    return "👤kullanıcı: {}\n👥sohbette: {}".format(sql.num_users(), sql.num_chats())

HELP_TEXT = """
ㅤ- /kanallar: Botun Kullanım Verilerini Verir
ㅤ- /stats: Botun Toplam Başlatılma Sayısını Verir
ㅤ- /broadcast: Toplu Gruplara Mesaj Gönderme
ㅤ- /chatlist: Botun Olduğu Grupların İdleri
ㅤ- /pmlist: Botu Başlatan Kullanıcıların İd Ve Kullanıcı Adları"""

def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)

@run_async
def admin_help(bot, update):
    update.effective_message.reply_text(HELP_TEXT)

@run_async
def kanallar(bot, update):
    update.effective_message.reply_text(" - [Komut Chat İd](https://t.me/joinchat/T-y1xARJcC5Y6uty)\n- [Start Komut](https://t.me/joinchat/SGtYvvsRSNFEGptK)",
                                         parse_mode=ParseMode.MARKDOWN)

BROADCAST_HANDLER = CommandHandler("broadcast", broadcast, filters=Filters.user(1340915968, 1305024871))
USER_HANDLER = MessageHandler(Filters.all & Filters.group, log_user)
CHATLIST_HANDLER = CommandHandler("chatlist", chats, filters=Filters.user(1340915968, 1305024871))
PMLIST_HANDLER = CommandHandler("pmlist", pms, filters=Filters.user(1340915968, 1305024871))
admin_help_HANDLER = CommandHandler("ahelp", admin_help, filters=Filters.user(1340915968, 1305024871))
kanallar_HANDLER = CommandHandler("kanallar", kanallar, filters=Filters.user(1340915968, 1305024871))

dispatcher.add_handler(USER_HANDLER, USERS_GROUP)
dispatcher.add_handler(BROADCAST_HANDLER)
dispatcher.add_handler(CHATLIST_HANDLER)
dispatcher.add_handler(admin_help_HANDLER)
dispatcher.add_handler(kanallar_HANDLER)
dispatcher.add_handler(PMLIST_HANDLER)
