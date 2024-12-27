import os
from dotenv import load_dotenv
from os import getenv

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    # Debugging: Print all environment variables loaded
    print("Loaded Environment Variables:")
    for key, value in os.environ.items():
        if "SECRET" not in key:  # Avoid printing sensitive data
            print(f"{key}: {value}")
    
    API_ID = int(os.environ.get("API_ID", "28045580"))
    API_HASH = os.environ.get("API_HASH", "83001e24418ec7f54bfe95d4e390419f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")  # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")  # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "7029090289"))  # Telegram ID, not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000"))  # in seconds
    AUTO_LEAVE = os.environ.get("AUTO_LEAVING_ASSISTANT", None)  # Change it to "True"
    COOKIES_FILE = getenv("COOKIES_FILE", "cookies.txt")  # Load the COOKIES variable
    
    # Debugging: Confirm the value of COOKIES
    print(f"COOKIES_FILE loaded: {COOKIES_FILE}")
