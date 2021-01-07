import logging
import os
import sys

import telegram.ext as tg

# günlük kaydı etkinleştir
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("En az 3.6 python sürümüne sahip olmalısınız! Birden çok özellik buna bağlıdır. Bot bırakma.")
    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)
    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', None))
    except ValueError:
        raise Exception("OWNER_ID env değişkeniniz geçerli bir tam sayı değil.")

    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")

    DB_URI = os.environ.get('DATABASE_URL')
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    WORKERS = int(os.environ.get('WORKERS', 8))
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)

else:
    from tg_bot.config import Development as Config
    TOKEN = Config.API_KEY
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("OWNER_ID değişkeniniz geçerli bir tam sayı değil.")

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    WORKERS = Config.WORKERS
    ALLOW_EXCL = Config.ALLOW_EXCL




updater = tg.Updater(TOKEN, workers=WORKERS)

dispatcher = updater.dispatcher


# Önceki tüm değişkenlerin ayarlandığından emin olmak için sonuna yükleyin
from tg_bot.modules.helper_funcs.handlers import CustomCommandHandler, CustomRegexHandler

# normal ifade işleyicisinin fazladan anahtarlar alabileceğinden emin olun
tg.RegexHandler = CustomRegexHandler

if ALLOW_EXCL:
    tg.CommandHandler = CustomCommandHandler
