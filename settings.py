import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.API_BASE_URL = os.getenv("API_BASE_URL")
        self.APP_ID = os.getenv("APP_ID")
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")
