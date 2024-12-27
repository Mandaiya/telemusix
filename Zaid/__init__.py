import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import Config
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging as std_logging
from Zaid.logging import LOGGER
from Zaid.cookies import load_cookies
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

# Use std_logging for built-in logging functionality
std_logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=std_logging.INFO
)

def LOGGER(name: str) -> logging.LOGGER:
    return logging.getLogger(name)

from Config import Config
BOT_USERNAME = Config.BOT_USERNAME
ASSISTANT_ID = Config.ASSISTANT_ID

# Load cookies before initializing the client
cookies = load_cookies()

# Initialize bot client
bot = TelegramClient('Zaid', api_id=Config.API_ID, api_hash=Config.API_HASH)
Zaid = bot.start(bot_token=Config.BOT_TOKEN)

# Initialize the assistant client using StringSession and cookies
client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)
client.start()

# Initialize call functionality
call_py = PyTgCalls(client)
call_py.start()
