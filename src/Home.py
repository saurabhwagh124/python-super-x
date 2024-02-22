import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('src/where-smywater-firebase-adminsdk-llijw-537a9cf8d0.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def 