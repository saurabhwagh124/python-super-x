import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from PyQt5.QtWidgets import QMessageBox

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


def check_login_details(u_name, password):
    print(u_name)
    print(password)
    user_ref  = db.collection("users").document(u_name)
    user_data = user_ref.get()
    print(user_data)
    print(user_data.exists)
    if user_data.exists:
        print(user_data.to_dict()['password'])
        if user_data.to_dict()['password'] == password:
            return True
        else:
            return False
    else: 
        return False
        
def upload_order_details(water,quantity,name,phone,address,date,time,supplier):
    order_details = {
        'water' : water,
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
    

    
def get_suppliers_orders(supplier_u_name,index):
    result_all = db._get_collection_reference('Orders').where('supplier','==',f'{supplier_u_name}').get()
    listx = []
    for index in result_all:
        #print (index.to_dict())
        listx.append(index.to_dict())
    print(listx)
    return listx




def upload_supplier_details(name,username,phone,area,password):
    admin_register = {
        'name':name,
        'username': username,
        'phone' : phone,
        'area' : area,
        'password': password
    }
    db.collection('Admin').document(f'{username}').set(admin_register)


def check_supplier_login(supplier_u_name,supplier_password):
    user_ref  = db.collection("Admin").document(supplier_u_name)
    user_data = user_ref.get()
    print(user_data)
    print(user_data.exists)
    if user_data.exists:
        print(user_data.to_dict()['password'])
        if user_data.to_dict()['password'] == supplier_password:
            return True
        else:
            return False
    else: 
        return False

def check_username_availability(u_name):
    user_ref = db.collection('users').document(u_name)
    user_data = user_ref.get()
    if user_data.exists:
        return True
    else:
        return False

def check_sup_username_availability(u_name):
    user_ref = db.collection('Admin').document(u_name)
    user_data = user_ref.get()
    if user_data.exists:
        return True
    else:
        return False 
        
        
