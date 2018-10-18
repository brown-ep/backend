from datetime import datetime
from os import environ

from pyrebase import initialize_app


# Firebase
FIREBASE_API_KEY = environ.get("FIREBASE_API_KEY", "no-key")
FIREBASE_AUTH_DOMAIN = ""
FIREBASE_DATABASE_URL = ""
FIREBASE_STORAGE_BUCKET = ""
FIREBASE_SERVICE_ACCOUNT = ""

__config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": FIREBASE_AUTH_DOMAIN,
    "databaseURL": FIREBASE_DATABASE_URL,
    "storageBucket": FIREBASE_STORAGE_BUCKET,
    "serviceAccount": FIREBASE_SERVICE_ACCOUNT,
}
__ = initialize_app(__config)
db = __.database()
