import os

from dotenv import load_dotenv

load_dotenv()

STAGE = os.getenv("STAGE", "test")
APP_NAME = os.getenv("APP_NAME")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

TABLE_NAME_MAIN = "main"

# DEFAULTS
DEFAULT_SYSTEM_ID = "system"
DEFAULT_UNIT = "unit"

# INFRASTRUCTURE
FUNCTION_CODE_ROOT_PATH = "financier"
FASTAPI_FUNCTION_CODE_PATH = "stacks.functions.app.app.handler"
