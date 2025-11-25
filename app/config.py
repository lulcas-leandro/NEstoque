import os
from dotenv import load_dotenv
from datetime import timezone, timedelta

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    TIMEZONE_OFFSET = int(os.environ.get('TIMEZONE_OFFSET', '-3'))
    TIMEZONE = timezone(timedelta(hours=TIMEZONE_OFFSET))