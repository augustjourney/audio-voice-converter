from dotenv import load_dotenv
import os
import json

# Loading .env props
load_dotenv()

class Config:
    DEBUG = False
    ENV = os.environ.get('ENV')
    HOST = '127.0.0.1'
    PORT = 8000
    SELECTEL_USER = os.environ.get('SELECTEL_USER')
    SELECTEL_PASSWORD = os.environ.get('SELECTEL_PASSWORD')
    ORIGINS = ['http://localhost:3000' 'https://api.createtoday.ru']