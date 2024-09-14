# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    TECH_VJ_BOT_TOKEN = os.environ.get("7363400875:AAFoRpKKfvEOgfzzIzYHxwp-h-CCUAxpUh0")
    TECH_VJ_BOT_USERNAME = os.environ.get("rk_url_bot") # Bot username without @.
    
    # The Telegram API things
    TECH_VJ_API_ID = int(os.environ.get("28993901"))
    TECH_VJ_API_HASH = os.environ.get("57256c4196b08ffaea61271aca07d7d1")
    
    # the download location, where the HTTP Server runs
    TECH_VJ_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    TECH_VJ_MAX_FILE_SIZE = 50000000
    TECH_VJ_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    TECH_VJ_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    TECH_VJ_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    TECH_VJ_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    TECH_VJ_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    TECH_VJ_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    TECH_VJ_OWNER_ID = int(os.environ.get("1273492006")) 
    TECH_VJ_SESSION_NAME = "VJ-URL-UPLOADER-BOT"
    
    # database uri (mongodb)
    TECH_VJ_DATABASE_URL = os.environ.get("mongodb+srv://kalerajkumar77777:qeDfp9e1dw2uKyoS@cluster0.ma4rc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    TECH_VJ_MAX_RESULTS = "50"

    # channel information
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("-1002476748124")) # your log channel id and make bot admin in log channel with full right 
    
   

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
