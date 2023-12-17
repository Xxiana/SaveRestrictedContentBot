#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from os import getenv 
from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables

API_HASH = getenv("API_HASH", "067109d3ffd777bf144a3251b50f69d5")
API_ID = int(getenv("API_ID", "29645247"))
BOT_TOKEN = getenv("BOT_TOKEN", "6647395152:AAHqzirUOMopY2HRJdq2CSDaGCvb0x9oMUU")
SESSION = getenv("SESSION", "BQAhIHQAPM4uwkHvZYxzOCGVR6cHCfLrpNIgOAMQjJRL-0sqtoJw2hU8xmOFS1lWIOX6SNYwLyu9SldMYV1zdsWqWNWbz4Awc6oE6YDAi806sD_flkuQrACQK0p3J8lXLFwvPKl99qMhvAuKY6ESkJ0MiSJfZqCsRwIIBQZKcyfjuqXVyGkRxucdIIU5w1mwvtw8RqiYSLLv0q-9EAE8iN-NHZbDj1i0Uxd0nxLGNwZ52-FRM7dXtJz47W5is_knsk5wU49c2s_V9X66Bb2mL10EQLda8hnioFMd4BP0mqOy4vtk8A_VZKdAB8EjUorQwUOG0DEl3qZfYVH9GfuPwG35_IOqewAAAABx00qeAA")
FORCESUB = getenv("FORCESUB", "afioverdosissave")
AUTH = int(getenv("AUTH", "1909672606"))

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
