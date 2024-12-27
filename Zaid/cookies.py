import os
import requests
from config import Config
from Zaid.logging import LOGGER
import sys

sys.path.append("..")


def save_file(pastebin_url, file_path="cookies/cookies.txt"):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "w") as file:
                file.write("")

        with open(file_path, "w") as file:
            file.write(response.text)
        return file_path

    except requests.exceptions.RequestException:
        return None


def save_cookies():
    print(vars(Config))
    full_url = str(Config.COOKIES)
    print(f"Full URL: {full_url}")
    paste_id = full_url.split("/")[-1]
    pastebin_url = f"https://batbin.me/raw/{paste_id}"

    file_path = save_file(pastebin_url)
    if file_path and os.path.getsize(file_path) > 0:
        LOGGER(_name_).info(f"Cookies saved successfully to {file_path}.")
    else:
        LOGGER(_name_).error("Failed to save cookies or the file is empty.")
