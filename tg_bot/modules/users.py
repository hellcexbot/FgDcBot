from io import BytesIO
from time import sleep
from typing import Optional
r, Filters, CommandHandler
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
                sleep(0)rd_from.username)



@run_async
def chats(bot: Bot, update: Update):
    all_chats = sql.get_all_chats() or []
    chatfile = 'Kullanıcı listesi:\n\n'
    for chat int(document=output, filename="chatlist.txt",
                                                caption="Veritabanımdaki sohbetlerin listesi burada.")

@run_async
def pms(bot: Bot, update: Update):
    all_pms = sql.get_all_pms() or []
    pmfile = 'Kullanıcı listesi:\n\n'
    for pm in all_pmVeritabanımdaki kullanıcıların listesi burada.")

def __stats__():
    return "👤kullanıcı: {}\n👥sohbette: {}".format(sql.num_users(), sql.num_chats())

HELP_TEXT = """
ㅤ- /kanallar: Botun Kullanım Verilerini Verir
ㅤ- /stats: Botun Toplam Başlatılma Sayısını Verir
ㅤ- /broadcast: Toplu Gruplara Mesaj Gönderme
ㅤ- /chatlistFilters.group, log_user)
CHATLIST_HANDLER = CommandHandler("chatlist", chats, filters=Filters.user(1340915968, 1305024871))
PMLIST_HANDLER = CommandHandler("pmlist", pms, filters=Filters.user(1340915968, 1305024871))
admin_help_HANDLER = Comman_help_HANDLER)
dispatcher.add_handler(kanallar_HANDLER)
dispatcher.add_handler(PMLIST_HANDLER)
