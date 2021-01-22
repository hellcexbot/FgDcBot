import logging
import os
import sys

        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("OWNER_ID değişkeniniz geçerli bir tam sayı değil.")

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PA
    EXCL = Config.ALLOW_EXCL




updater = tg.UpdrN, workers=WORKERS)

dispatcher = updater.dis
# normal ifade işleyicisinin fazladan anahtarlar alabileceğinden emin olun
tg.RegexHandler = CustomRegexHandle
if ALLC:
    tg.CommandHammandHandler
