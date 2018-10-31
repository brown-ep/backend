from datetime import datetime
from os import environ

from pyrebase import initialize_app


# Firebase
FIREBASE_API_KEY = "AIzaSyDNOXCCYb7VulBQx3sNFZ-ORaYEsvRRGP4"
#environ.get("FIREBASE_API_KEY", "no-key")
FIREBASE_AUTH_DOMAIN = "brown-ep-startup-ideas-app.firebaseapp.com"
FIREBASE_DATABASE_URL = "https://brown-ep-startup-ideas-app.firebaseio.com"
FIREBASE_STORAGE_BUCKET = "brown-ep-startup-ideas-app.appspot.com"
FIREBASE_SERVICE_ACCOUNT = "brown-ep-startup-ideas-app-firebase-adminsdk-qu2p2-6f5baf423c.json"

__config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": FIREBASE_AUTH_DOMAIN,
    "databaseURL": FIREBASE_DATABASE_URL,
    "storageBucket": FIREBASE_STORAGE_BUCKET,
    "serviceAccount": FIREBASE_SERVICE_ACCOUNT,
}
__ = initialize_app(__config)
db = __.database()
