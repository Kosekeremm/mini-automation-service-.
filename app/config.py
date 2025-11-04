import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class Config:
    ENV = os.getenv("FLASK_ENV", "production")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    SMTP_HOST = os.getenv("SMTP_HOST", "")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASS = os.getenv("SMTP_PASS", "")
    APSCHEDULER_ENABLED = os.getenv("APSCHEDULER_ENABLED", "True").lower() == "true"
