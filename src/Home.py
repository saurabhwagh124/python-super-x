import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



def register_to_db(u_name, f_name, password,phone):
    cred = credentials.Certificate("src/where-smywater-firebase-adminsdk-llijw-537a9cf8d0.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    user_profile = {
        'username': u_name,
        'firstname': f_name,
        'password': password,
        'phone': phone
    }
    db.collection('users').document(f'{u_name}').set(user_profile)

        
