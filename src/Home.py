import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("src/where-smywater-firebase-adminsdk-llijw-537a9cf8d0.json")
firebase_admin.initialize_app(cred)

def register_to_db(u_name, f_name, password,phone):
    # cred = credentials.Certificate("src/where-smywater-firebase-adminsdk-llijw-537a9cf8d0.json")
    # firebase_admin.initialize_app(cred)
    db = firestore.client()
    user_profile = {
        'username': u_name,
        'firstname': f_name,
        'password': password,
        'phone': phone
    }
    db.collection('users').document(f'{u_name}').set(user_profile)

def check_login_details(u_name,password):
    # cred = credentials.Certificate("src/where-smywater-firebase-adminsdk-llijw-537a9cf8d0.json")
    # firebase_admin.initialize_app(cred)
    db = firestore.client()
    result1 = db.collection('users').where("username","==",f"{u_name}")
    result2 = db.collection('users').where("password","==",f"{password}")
    print(result2)
    print(result1)
    if(result1 and result2 != None):
        return True
    else:
        return False
        
def upload_order_details(quantity,name,phone,address,date,time):
    dbu = firestore.client()
    order_details = {
        'quantity' : quantity,
        'name': name,
        'phone': phone,
        'address': address,
        'date': date,
        'time': time
    }
    dbu.collection('Orders').document(f'{name}').set(order_details)
def get_order_details(x):
    dbg = firestore.client()
    resultx = dbg.collection('Orders').where('name','==',f'{x}').get()
    for i in resultx:
        print(i.to_dict())
        return i.to_dict()
    
def get_suppliers_orders():
    db_for_suppliers = firestore.client()
    result_all = db_for_suppliers.collection('Orders').where('name','==','').get()
    for j in result_all:
        return j.to_dict()
