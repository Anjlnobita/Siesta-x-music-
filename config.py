import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("2556"))
API_HASH = getenv("28e494c6c0cc076234d7b66bb9299")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7836352880:AAEObCD7CCAIOgBjsrSBdX1jLrJdks")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Anjlnobita_i")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME","Siesta_kimi_bot")
# --------------------------------------------------------
BOT_NAME = getenv("𝐬𝐢𝐞𝐬𝐭𝐚 ✗ ⸤ 𝐦𝐮𝐬𝐢𝐜 ⸣ ⁿᵒ ͢ᵃᵈˢ")
# ---------------------------------------------------------


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://anjlnobita:tCUPU9Ty1FFvLumv@cluster0.appf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -100237233866))

# Get this value from @PURVI_HELP_BOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 677786063))


# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://graph.org/PRIVACY-FOR-TEAM-PURVI-BOTS-09-18")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Marwin040/AmritaXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/anjlnobita")
SUPPORT_CHAT = getenv("SUPPORT_CHAT","https://t.me/teenscmnity")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 555))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", BQFtvSkAG6R5VnPftqE92LJzOijWC9ZJ8o-Rr_2WY1bW6nRd22c5K2JS1gRo-k47j8vc9moJybFeaaGSqS25HleUKz1Z2oaHNMOBNvBAuFNyxmV7Z_SNUFfH3QDpS1wDGTamYhA_cj8-Ys2eJ88qYk7zI0tffhfcEQZ8EDkCm_3mfsZizS47EwZ1OJS4oQIAXmP0sWrU3hZ07UTlkx_ssLAvCryqB_wUV6Ad2-eh_kk0IrsQ9sB9R_y83UOAZTXNDqAtJYoYT_CoKXhqdLVn-ZlVq9wVYQH06s-S20gHYYZsCjUF_r6C9SNVD5Uy41M59TQmk0u9M9U5vXFZTywAAAAHJCOD2AA)
STRING2 = getenv("STRING_SESSION2", BQFzesEAsIBP9gJMA_0ifntT7yJ-IAH-nOuWPKe5u3eOyLpl_fDysOJxNsuuxh_p_Rk3HlVSeSSFH-2XPRPzgnT-qXsECMB-YKiegcisfTL7I1StDEwTtw4XTokZRQLxr0H_vVD4SCd5cMnly1sP8_vS7aSs9Ke8Zyu0t5_48snPTXTaKlDmCQricJEB2L3a_x0nRj_f5Sj68WyTrAYFhVHXrmD-ABqbssmdT_rmtA5JYXQ99GNgDh-xqjw2D_oNABD8GxjI6-D6boWQAKzjnDKVqM4Dqc8NyB700nM8674SEpAXiL1EO3Tu6wUNXU8RYc3y80VVeAyTIxnBbDXpCDgAAAAGn_jFfAA)
STRING3 = getenv("STRING_SESSION3", BQGAsdwAhn5Du632u6d8PGwxNxHuKp33TaQqTIoBICzkABcuQBGS-6uGzMelR14vC6F0N1yrc47mVIOvL05Ies8WE4GFh8446qotl_6J-0OiAwTArmiDQE3TT-NRpIPJ4aq3SyqyLLuwbiX4HonsYeE7TGH6ZEALvt1YrlOYyV0A3k786s-e-0yVU8Mj-1-qWlQoH74-10iv60Z91ESYF8dvEJOlvWSQwXWIpp4K_Ki47xFiiwigCGEiQYlniTSZwIGrcFzOsZv8Sr6LIsLJzqqvNEPqDWrLopucciGKMrS-ao2BvS0egmbqtWkauR8jr3YqnhVF8qrWIKYuVH9XcUpJmAAAAAB_VyXgAA)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/5SL.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/5S5.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/_IP.jpg"
STATS_IMG_URL = "https://envs.sh/5SK.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure tha
