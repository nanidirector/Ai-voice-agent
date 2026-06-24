from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SARVAM_API_KEY = os.getenv("SARVAM_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")