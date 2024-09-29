from dotenv import load_dotenv
import os

load_dotenv()

STAGE = os.getenv("STAGE")
APP_NAME = os.getenv("APP_NAME")
