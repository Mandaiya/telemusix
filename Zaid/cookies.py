import logging 
import Config

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def load_cookies():
    cookies_file = Config.COOKIES
    if os.path.exists(cookies_file):
        with open(cookies_file, 'r') as file:
            cookies = file.read()
            logging.info("Cookies loaded successfully.")
            return cookies
    logging.warning("Cookies file not found.")
    return None
