import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  or "Put a strong default key here"