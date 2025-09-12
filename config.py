# =======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# --- LOAD ENVIRONMENT VARIABLES ---

load_dotenv()

# -------------------- [ BASIC CONFIG ] --------------------

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# -------------------- [ OWNER & BOT INFO ] --------------------

OWNER_ID = int(getenv("OWNER_ID", 7473021518))
OWNER_USERNAME = getenv("OWNER_USERNAME", "TheSigmaCoder")

BOT_USERNAME = getenv("BOT_USERNAME", "Sonali_Music_Bot")
BOT_NAME = getenv("BOT_NAME", "˹sᴏɴᴧʟɪ ꭙ ᴍᴜsɪᴄ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "Sonali")

# -------------------- [ DATABASE / HEROKU / REPO ] --------------------

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Im-Notcoder/SonaliV2")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", "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")

# -------------------- [ LOGGER & LINKS ] --------------------

LOGGER_ID = int(getenv("LOGGER_ID", -1002141133985))

PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-YukkiMusic-08-30")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PURVI_BOTS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PURVI_UPDATES")

# -------------------- [ LIMITS & TIME SETTINGS ] --------------------

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
DURATION_LIMIT = int(60 * DURATION_LIMIT_MIN)  # converted into seconds

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# -------------------- [ SPOTIFY CONFIG ] --------------------

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# -------------------- [ STRING SESSIONS ] --------------------

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# -------------------- [ IMAGES / THUMBNAILS ] --------------------

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/x5lytj.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/leaexg.jpg")

PLAYLIST_IMG_URL = "https://files.catbox.moe/b0e4vk.jpg"
STATS_IMG_URL = "https://files.catbox.moe/psya34.jpg"

TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

# -------------------- [ UTILITIES ] --------------------

BANNED_USERS = filters.user()

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


# -------------------- [ FUNCTIONS ] --------------------

def time_to_seconds(time: str) -> int:
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


# -------------------- [ VALIDATIONS ] --------------------

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL url is wrong. Must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT url is wrong. Must start with https://")

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Sonali-MusicV2
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
