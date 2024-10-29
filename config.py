import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID" 25392624))
API_HASH = getenv("API_HASH" c9208c6e73e4d48a7a03c3ee296995be)
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN" 6802653453:AAGLR2i95-UL0RwDnFPcYCWBi3EjyevGlvY)
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","II_ROYALENTRY1128_II")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Queenhoneybot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "Queen music")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "KHWAAISH_HOON")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", Nonemongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority)
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", --1002132108601))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 1384525218))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Yewsdhi/Royalkingpiyu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/royalmusibotl")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/royalmusicboto")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", NoneBQF3jTgADZsJsvJPGvlFsb1S6LjnKH268ot5YfyvyXWuZ2etZr88WXKuqlkEo8UfG9GdcOg8-E5R6rqxAZy7lczlnYRM4FdCgazpeBIj2Iasqy_PuTvlHaQQDfQs9DEwrSAISOCtFoQj4QWhjfkLD0vH8J-FzN0yPiMyCCdK5RCXqTJEVbcfcpvvcRrjumSbpqe0aSfy49cQz2s5-mT_w36wSyEPhrsHsCVgJF08lm5EI_o4N9x72pIqsIrkgWJkIqZ1rq7wx9VBlQUpX-uAgnl22HhjqAEK7YRduJ0HE2X54eyopxz34IKzVk8U7tMhRgpM13xG196ovQF2P9s22WswyGK83QAAAAHL4VSiAA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/e78646567b7bcad4c6a55.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/8ad010a2a1fe583469930.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
STATS_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
STREAM_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org//file/5be677d49aa2e5c13cf75.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
