import os

LOG_LEVEL = "INFO"

ORIGIN = os.environ.get("ORIGIN", "239.255.255.250")

DB_NAME = os.environ.get("DB_NAME")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
