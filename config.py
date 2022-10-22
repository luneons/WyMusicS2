import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "DODEKATHEON MUSIC")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/20147c4f049e2c1f2f248.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/6809135960af808e931b9.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/7ffd2c88f5275fc9058eb.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/1e01db4b4bde83842e8d7.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "dodekatheonbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "dodekatheonassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "dodekatheonpublik")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "dodekatheon3")
OWNER_NAME = getenv("OWNER_NAME", "luneons") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "MELE")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
