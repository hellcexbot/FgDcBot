if not __name__.endswith("sample_config"):
    import sys
    print("BENİOKU okunmak üzere oradadır. Bu örnek yapılandırmayı bir yapılandırma dosyasına genişletin, yalnızca burada değerleri yeniden adlandırıp değiştirmekle kalmayın. Bunu yapmak sana geri tepecektir. "
          "\nBot bırakılıyor...", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = ""
    OWNER_ID = "1340915968" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "fireganqQ"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    CERT_PATH = None
    PORT = 5000
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
