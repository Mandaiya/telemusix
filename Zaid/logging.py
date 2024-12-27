import logging
import os

# Define log file path
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "telethon_music.log")

# Create a custom logger
LOGGER = logging.getLogger("TelethonMusic")
LOGGER.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_format)

# File handler
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
file_handler.setFormatter(file_format)

# Adding handlers to the logger
LOGGER.addHandler(console_handler)
LOGGER.addHandler(file_handler)

# Example usage
if __name__ == "__main__":
    LOGGER.info("Logger setup complete!")
    LOGGER.debug("This is a debug message.")
    LOGGER.error("This is an error message.")
    
