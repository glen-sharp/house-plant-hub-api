import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = "INFO"

ORIGIN = os.environ.get("ORIGIN", "localhost")

DB_NAME = os.environ.get("DB_NAME", "house-plant-hub")
USERNAME = os.environ.get("USERNAME", "pi4b")
PASSWORD = os.environ.get("PASSWORD", "password")
HOST = os.environ.get("HOST", "192.168.0.152")

SECRET_KEY = os.environ["SECRET_KEY"]

FULL_MOISTURE_LEVEL = 340
NO_MOISTURE_LEVEL = 790

RECORD_HISTORY_DAYS = 7
