import http.cookiejar as cookiejar
import requests
from Zaid.logging import LOGGER
from config import Config

def load_cookies():
    """Load cookies from the cookies.txt file."""
    cookies_file = Config.COOKIES_FILE
    cookie_jar = cookiejar.MozillaCookieJar(cookies_file)
    try:
        cookie_jar.load(ignore_discard=True, ignore_expires=True)
        print("Cookies loaded successfully!")
    except FileNotFoundError:
        print(f"Cookies file not found: {cookies_file}")
    return cookie_jar

def make_request_with_cookies(url):
    """Make a request using loaded cookies."""
    cookies = load_cookies()
    session = requests.Session()
    session.cookies = cookies
    response = session.get(url)
    return response.text
