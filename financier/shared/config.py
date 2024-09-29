from dotenv import load_dotenv
import os

load_dotenv()

STAGE = os.getenv("STAGE")
APP_NAME = os.getenv("APP_NAME")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

TABLE_NAME_MAIN = "main"

# DEFAULTS
DEFAULT_SYSTEM_ID = "system"
DEFAULT_UNIT = "unit"
