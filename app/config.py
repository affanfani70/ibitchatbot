import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key')
    DATA_PATH = os.getenv('DATA_PATH', 'data/Ibit_data.json')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
