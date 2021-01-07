from io import BytesIO
from time import sleep
from typing import Optional

from telegram import TelegramError, Chat, Message
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
    if len(to_send) >= 2:
        chats = sql.get_all_chats() or []
        failed = 0
        for chat in chats:
            try:
                bot.sendMessage(int(chat.chat_id), to_send[1])
                sleep(0.1)
            except TelegramError:
                failed += 1
                LOGGER.warning("%s grubuna yayın gönderilemedi, grup adı %s", str(chat.chat_id), str(chat.chat_name))

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
    chatfile = 'Sohbet listesi.\n'
    for chat in all_chats:
        chatfile += "{} - ({})\n".format(chat.chat_name, chat.chat_id)

    with BytesIO(str.encode(chatfile)) as output:
        output.name = "chatlist.txt"
        update.effective_message.reply_document(document=output, filename="chatlist.txt",
                                                caption="Veritabanımdaki sohbetlerin listesi burada.")


def __stats__():
    return "👤kullanıcı: {}\n👥sohbette: {}".format(sql.num_users(), sql.num_chats())

HELP_TEXT = """
/stats: Botun Toplam Başlatılma Sayısını Verir
/broadcast: Toplu Gruplara Mesaj Gönderme
/chatlist: Botun Olduğu Grupların İdleri"""

def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)

@run_async
def admin_help(bot, update):
    update.effective_message.replay_text(HELP_TEXT)

BROADCAST_HANDLER = CommandHandler("broadcast", broadcast, filters=Filters.user(1340915968))
USER_HANDLER = MessageHandler(Filters.all & Filters.group, log_user)
CHATLIST_HANDLER = CommandHandler("chatlist", chats, filters=Filters.user(1340915968))
admin_help_HANDLER = CommandHandler("ahelp", admin_help, filters=Filters.user(1340915968))

dispatcher.add_handler(USER_HANDLER, USERS_GROUP)
dispatcher.add_handler(BROADCAST_HANDLER)
dispatcher.add_handler(CHATLIST_HANDLER)
dispatcher.add_handler(admin_help_HANDLER)