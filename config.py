import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = "5435355012:AAG4TwxBNsJoPBouwNurL1xk_wvuRS8cBfc"

    # The Telegram API things
    APP_ID = 17945796
    API_HASH = "4a05481a5da2d66f801acffc4ca5ee4b"
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1813305809").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = "mongodb+srv://sakura:sakura@cluster0.futdd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

