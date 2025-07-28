import re
from os import environ
from Script import script

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Main
SESSION = environ.get("SESSION", "Media_search")
API_ID = int(environ.get("API_ID", "13992749"))
API_HASH = environ.get("API_HASH", "c8b1a7c3ce9aa1d1eec2fee774d48399")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
PORT = environ.get("PORT", "8082")

# Owners
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get("ADMINS", "5466885993").split()
]
OWNER_USERNAME = environ.get(
    "OWNER_USERNAME", "ravikumarcn"
)  # without @ or https://t.me/
USERNAME = environ.get("USERNAME", "ravikumarcn")  # ADMIN USERNAME

# Database Channel
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get("CHANNELS", "-1002430088725").split()
]

# ForceSub Channel & Log Channels
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002245219361"))
AUTH_REQ_CHANNEL = int(environ.get("AUTH_REQ_CHANNEL", "-1002245219361"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001913629397"))
LOG_API_CHANNEL = int(environ.get("LOG_API_CHANNEL", "-1001913629397"))
LOG_VR_CHANNEL = int(environ.get("LOG_VR_CHANNEL", "-1001913629397"))

# MongoDB
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://King1:King1@cluster0.udffg72.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "ravikumar1cn")

# Files index database url
FILES_DATABASE = environ.get("FILES_DATABASE", "mongodb+srv://King2:King2@cluster0.daup34w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "ravikumar1cn")

# Other Channel's
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1001913629397"))
DELETE_CHANNELS = int(environ.get("DELETE_CHANNELS", "0"))
request_channel = environ.get("REQUEST_CHANNEL", "-1001913629397")
REQUEST_CHANNEL = (
    int(request_channel)
    if request_channel and id_pattern.search(request_channel)
    else None
)
MOVIE_UPDATE_CHANNEL = int(environ.get("MOVIE_UPDATE_CHANNEL", "-1002565642490"))

# Added Link Here Not Id
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "https://t.me/KannadaMagaaBot")
MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "https://t.me/KannadaMagaaZone")

# Verification
IS_VERIFY = is_enabled("IS_VERIFY", True)
# ---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How_To_Open_Links_bypass")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/How_To_Open_Links_bypass")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/How_To_Open_Links_bypass")
VERIFY_IMG = environ.get(
    "VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"
)
SHORTENER_API = environ.get("SHORTENER_API", "a029412747a7633322dfb153f38790ef90bf99cc")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "vplink.in")
SHORTENER_API2 = environ.get(
    "SHORTENER_API2", "a029412747a7633322dfb153f38790ef90bf99cc"
)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "vplink.in")
SHORTENER_API3 = environ.get(
    "SHORTENER_API3", "a029412747a7633322dfb153f38790ef90bf99cc"
)
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "vplink.in")
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "1"))
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "1"))

# Language & Quality & Season & Year
LANGUAGES = [
    "hindi",
    "english",
    "telugu",
    "tamil",
    "kannada",
    "malayalam",
    "bengali",
    "marathi",
    "gujarati",
    "punjabi",
    "marathi",
]
QUALITIES = [
    "HdRip",
    "web-dl",
    "bluray",
    "hdr",
    "fhd",
    "240p",
    "360p",
    "480p",
    "540p",
    "720p",
    "960p",
    "1080p",
    "1440p",
    "2K",
    "2160p",
    "4k",
    "5K",
    "8K",
]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Pictures And Reaction
START_IMG = (
    environ.get(
        "START_IMG",
        "https://i.ibb.co/RGfRT2jk/photo-2025-01-23-05-42-03-7530477859291267076.jpg",
    )
).split()
FORCESUB_IMG = environ.get("FORCESUB_IMG", "https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg")
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split()
PAYPICS = (
    environ.get("PAYPICS", "https://i.ibb.co/HpNcwvzR/photo-2025-05-06-15-41-18-7530474547871481880.jpg")
).split()
SUBSCRIPTION = environ.get(
    "SUBSCRIPTION", "https://i.ibb.co/Pzshgyfb/photo-2024-06-12-17-04-00-7530477949485580316.jpg"
)
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]


# Other Funtions
FILE_AUTO_DEL_TIMER = int(environ.get("FILE_AUTO_DEL_TIMER", "60"))
AUTO_FILTER = is_enabled("AUTO_FILTER", True)
IS_PM_SEARCH = is_enabled("IS_PM_SEARCH", True)
IS_SEND_MOVIE_UPDATE = is_enabled(
    "IS_SEND_MOVIE_UPDATE", True
)  # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
MAX_BTN = int(environ.get("MAX_BTN", "8"))
AUTO_DELETE = is_enabled("AUTO_DELETE", True)
DELETE_TIME = int(environ.get("DELETE_TIME", 180))
IMDB = is_enabled("IMDB", False)
FILE_CAPTION = environ.get("FILE_CAPTION", f"{script.FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
PROTECT_CONTENT = is_enabled("PROTECT_CONTENT", False)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
LINK_MODE = is_enabled("LINK_MODE", True)
TMDB_API_KEY = environ.get("TMDB_API_KEY", "")

# Online Streaming And Download
STREAM_MODE = bool(environ.get("STREAM_MODE", True))  # Set True or Flase

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if "DYNO" in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "https://yelling-dalia-kannadamagaa1-7b257971.koyeb.app/")

# Commands
admin_cmds = [
    "/add_premium - Add A User To Premium",
    "/premium_users - View All Premium Users",
    "/remove_premium - Remove A User's Premium Status",
    "/add_redeem - Generate A Redeem Code",
    "/refresh - Refresh Free Trail",
    "/set_muc - Set Movie Update Channel",
    "/pm_search_on - Enable PM Search",
    "/pm_search_off - Disable PM Search",
    "/set_ads - Set Advertisements",
    "/del_ads - Delete Advertisements",
    "/setlist - Set Top Trending List",
    "/clearlist - Clear Top Trending List",
    "/verify_id - Verification Off ID",
    "/index - Index Files",
    "/send - Send Message To A User",
    "/leave - Leave A Group Or Channel",
    "/ban - Ban A User",
    "/unban - Unban A User",
    "/broadcast - Broadcast Message",
    "/grp_broadcast - Broadcast Messages To Groups",
    "/delreq - Delete Join Request",
    "/channel - List Of Database Channels",
    "/del_file - Delete A Specific File",
    "/delete - Delete A File(By Reply)",
    "/deletefiles - Delete Multiple Files",
    "/deleteall - Delete All Files",
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"},
]
