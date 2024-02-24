import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate("src/where-smywater-firebase-adminsdk-llijw-537a9cf8d0.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def register_to_db(u_name, f_name, password,phone):
    user_profile = {
        'username': u_name,
        'firstname': f_name,
        'password': password,
        'phone': phone
    }
    db.collection('users').document(f'{u_name}').set(user_profile)

def check_login_details(u_name,password):
    result1 = db.collection('users').where("username","==",f"{u_name}")
    result2 = db.collection('users').where("password","==",f"{password}")
    print(result2)
    print(result1)
    if(result1 and result2 != None):
        return True
    else:
        return False
        
def upload_order_details(quantity,name,phone,address,date,time,supplier):
    order_details = {
        'quantity' : quantity,
        'name': name,
        'phone': phone,
        'address': address,
        'date': date,
        'time': time,
        'supplier': supplier
    }
    db.collection('Orders').document(f'{name}').set(order_details)
def get_order_details(x):
    resultx = db.collection('Orders').where('name','==',f'{x}').get()
    for i in resultx:
        print(i.to_dict())
        return i.to_dict()
    
def get_suppliers_orders():
    result_all = db._get_collection_reference('Orders')



def upload_supplier_details(name,username,phone,password):
    admin_register = {
        'name':name,
        'username': username,
        'phone' : phone,
        'password': password
    }
    db.collection('Admin').document(f'{username}').set(admin_register)
        
