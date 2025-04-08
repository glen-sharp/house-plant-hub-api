import os

LOG_LEVEL = "INFO"

ORIGIN = os.environ.get("ORIGIN", "239.255.255.250")

DB_NAME = os.environ.get("DB_NAME", "house-plant-hub")
USER = os.environ.get("USER", "pi4b")
PASSWORD = os.environ.get("PASSWORD", "password")
HOST = os.environ.get("HOST", "192.168.0.152")
