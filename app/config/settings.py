import os

from dotenv import load_dotenv

load_dotenv()

# Variables
DEBUG = os.getenv('DEBUG')
SECRET_KEY = os.getenv('SECRET_KEY')
PORT = os.getenv('PORT')

# Database
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')