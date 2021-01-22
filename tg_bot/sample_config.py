if not __name__.endswith("sample_config"):
    import sys
    pTIONAL
    CERT_PATH = None
    PORT = 5000
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
