import importlib
import re
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import 

from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL
# modülleri dinamik olarak yüklemek için gerekli
# NOT: Modül sırası garanti edilmez, bunu yapılandırma dosyasında belirtin!
from tg_bot.modules import ALL_MODULES
from tg_bot.modules.helper_funcs.chat_status import is_user_admin

# Bot Versiyonu
BOT_VERSİYON = "0.1.3"

# Pmde Botu Başlatanları Göndereceği Chat İd
START_CHAT_İD = "-1001415745495"

# START_CHAT_İD TEXT
START_CHAT_İD_TEXT = """
👤 **Kullanıcı:** [{}](tg://user?id={})
👤 **İd'si:** `{}`
"""

# Hangi Grupda Hangi Kim Hangi Komutu Kullandı
KOMUT_CHAT_İD = "-1001362147031"

# KOMUT_CHAT_İD TEXT
KOMUT_CHAT_İD_TEXT = """
👤 **Kullanıcı:** [{}](tg://user?id={})
👤 **İd'si:** `{}`
👥 **Chat:** #{}
👥 **Chat İd:** `{}`
⚙️ **Komut: #{}**
"""

PM_START_TEXT = """
**Selam!
🤖 Ben ‘Doğrulukmu ve ya Cesaretmi’ oyunu için bir botum! ☠️Oyunu başlatmak için beni qruba ekleyerek /start yaz. Yardım için /help yazmanız yeterlidir!**
"""

HELP_STRINGS = """
**Selam [{}](tg://user?id={})!**

**Komutlar:**
 - /start: botu başlat
 - /help: Size bu mesajı atar.
 - /dc: Size Doğruluk Veya Cesaret Sorusu Seçimi Yaptırı
 - /sahip: Sahibimi, Duyuru Kanalımı Ve Sahibimin Blog Kanalını Verir
 - /stat: Bottaki Toplam Soru Sayısını Ve Versiyonunu Verir
 - /banket: Botla İlgili Anketleri Verir
 - /reklam: Bota Verilmiş Reklamlar
 
**‼️ Oyun Komutu Pm'de Calışmaz :(**
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
        raise maz! Lütfen birini değiştir")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_moduwer()] = imported_module


@run_async
def start(bot: Bot, update: Update):
    user = update.effective_user
    first_name = user.first_name
    user_id = user.id
    chat = update.effective_chat
    msg = update.effective_message

    if chat.type == "private":
    first_name = user.first_name
    user_id = user.id
    msg = update.effective_message

    msg.reply_text(HELP_STRINGS.format(first_name, user_id),
                    parse_mode=ParseMode.MARKDOWN)



def migrate_chats(bot: Bot, update: Update):
    msg = update.effective_message  # type: Optional[Message] 
    if msg.migrate_to_chat_ider = CommandHandler("help", get_help)
    migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(migrate_handler)


    if WEBHOOK:ut=15, read_latency=4)

    updater.idle()


if __name__ == '__main__':
    LOGGER.info("Başarıyla yüklenen modüller: " + str(ALL_MODULES))
    main()
