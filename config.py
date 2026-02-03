import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN","7137583125:AAGZ_XEkte_MnHQr5fIFnwkADlBUgQXe6AY")
BOT_NAME = getenv("BOT_NAME","KRS_SaveRestricted_Bot")
API_ID = int(getenv("API_ID","17108931"))
API_HASH = getenv("API_HASH","436b24700208cae55ded351d8f25fd7a")
MONGODB_URL = getenv("MONGODB_URL","mongodb+srv://nsbots1947:xLMzAb5YJzL2wa1u@rss003.fgofoux.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME","Kushi_Yarige_bedda")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME","KRS_SaveRestricted_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "hbjmnkk")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ybjmnkkn")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5300197778").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
