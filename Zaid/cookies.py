import logging 
import Config

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def load_cookies():
    cookies_file = Config.cookie
    if os.path.exists(cookie):
        with open(cookie, 'r') as file:
            cookies = file.read()
            logging.info("Cookie loaded successfully.")
            return cookies
    logging.warning("Cookie file not found.")
    return None
