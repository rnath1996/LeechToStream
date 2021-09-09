import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "1991731194:AAEpPT7JK1pBoRpqpe-61-N_z3OZt7QP2w4"
    # The Telegram API things
    APP_ID = 3447744
    API_HASH = "6e06f472f9bc2b6d495607bbd8f9b621"
    OWNER_ID = 1930040165
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001140305679]
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 15))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = "leech@rahulnathleechbot"
    YTDL_COMMAND = "ytdl@rahulnathleechbot"
    PYTDL_COMMAND = "pytdl@rahulnathleechbot"
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    INDEX_LINK = os.environ.get("INDEX_LINK", "")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = "savethumbnail@rahulnathleechbot"
    CLEAR_THUMBNAIL = "clearthumbnail@rahulnathleechbot"
    CLEAR_UNDELETED = os.environ.get("CLEAR_UNDELETED", "clearall")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "getlog") 
