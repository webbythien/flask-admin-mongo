

import os

from dotenv import load_dotenv
load_dotenv()

# Enable debug mode
DEVELOPMENT = True
DEBUG = True

# Create dummy secrey key so we can use sessions
SECRET_KEY = os.getenv('SECRET_KEY')

# Create in-memory database
# DATABASE_FILE = 'flaskcms.sqlite'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_TRACK_MODIFICATIONS = False
MONGO_URI=os.getenv('MONGO_URI')
MONGO_DB_NAME=os.getenv('MONGO_DB_NAME')
MONGODB_SETTINGS = [
    {"db": MONGO_DB_NAME, "host": MONGO_URI+MONGO_DB_NAME, "alias": "default"},
    {
        "db": MONGO_DB_NAME+'2',
        "host": MONGO_URI+MONGO_DB_NAME,
        "alias": "secondary",
    },
]
# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"
SECURITY_RESET_URL = "/reset/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"
SECURITY_POST_RESET_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = False
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False

# AWS S3 Bucket
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')
AWS_S3_BUCKET = os.getenv('AWS_S3_BUCKET')
