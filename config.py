import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "Put a strong default key here"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or "mysql://razerx100:35401350@localhost/meds"
    )
