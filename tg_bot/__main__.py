import importlib
import re
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL
# modülleri dinamik olarak yüklemek için gerekli
# NOT: Modül sırası garanti edilmez, bunu yapılandırma dosyasında belirtin!
from tg_bot.modules import ALL_MODULES
from tg_bot.modules.helper_funcs.chat_status import is_user_admin

BOT_VERSİYON = "0.1.0"
PM_START_TEXT = """
Merhaba {}!

Herhangi bir hata veya sorunuz varsa Sahibim İle İletişime Gecmekden Cekinmeyin! 😊

Ayrıca Yeni Özellikler, Kesinti Süresi Vb. için Duyuru Kanalıma Baka Bilirsin!! 😎

Kullanılabilir komutların listesini /help ile bulabilirsiniz.
"""

HELP_STRINGS = """
𝐒𝐞𝐥𝐚𝐦 {}!

𝐊𝐨𝐦𝐮𝐭𝐥𝐚𝐫:
 - /start: botu başlat
 - /help: Size bu mesajı atar.
 - /dc: Size Doğruluk Veya Cesaret Sorusu Seçimi Yaptırı
 - /sahip: Sahibimi, Duyuru Kanalımı Ve Sahibimin Blog Kanalını Verir
 - /stat: Bottaki Toplam Soru Sayısını Ve Versiyonunu Verir
 <a href="tg://user?id=1340915968">text</>
‼️ /dc 𝐊𝐨𝐦𝐮𝐭𝐮 𝐏𝐦'𝐝𝐞 𝐂𝐚𝐥𝐢𝐬̧𝐦𝐚𝐳 :(
"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []

CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("tg_bot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Aynı isimde iki modül olamaz! Lütfen birini değiştir")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


@run_async
def start(bot: Bot, update: Update):
    user = update.effective_user
    first_name = user.first_name
    user_id = user.id
    msg = update.effective_message

    msg.reply_text(text=PM_START_TEXT.format(first_name),
        reply_markup=InlineKeyboardMarkup([
                                           [InlineKeyboardButton(text="📢 Duyuru Kanalım",
                                                                 url="t.me/fireqanQBotlari")],
                                           [InlineKeyboardButton(text="🤖 Beni Gruba Ekle",
                                                                 url="tg://resolve?domain=FgDc_Bot&startgroup=a")],
                                           [InlineKeyboardButton(text="🍾 Oyun Grubumuz",
                                                                 url="t.me/FgDcBotGrup")],
                                           [InlineKeyboardButton(text="👮‍♂️ Sahibim",
                                                                 url="t.me/fireganqq")]]))

@run_async
def get_help(bot: Bot, update: Update):
    user = update.effective_user
    first_name = user.first_name
    msg = update.effective_message

    msg.reply_text(HELP_STRINGS.format(first_name))



def migrate_chats(bot: Bot, update: Update):
    msg = update.effective_message  # type: Optional[Message] 
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("%s 'den %s'ye taşınıyor", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Başarıyla taşındı!")
    raise DispatcherHandlerStop


def main():
    start_handler = CommandHandler("start", start)

    help_handler = CommandHandler("help", get_help)
    migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(migrate_handler)


    if WEBHOOK:
        LOGGER.info("Webhooks Kullanma.")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN,
                                    certificate=open(CERT_PATH, 'rb'))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Uzun yoklama kullanma.")
        updater.start_polling(timeout=15, read_latency=4)

    updater.idle()


if __name__ == '__main__':
    LOGGER.info("Başarıyla yüklenen modüller: " + str(ALL_MODULES))
    main()
