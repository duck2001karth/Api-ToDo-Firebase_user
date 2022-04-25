import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

#Configuraciones para firebase
cred = credentials.Certificate("acount_key_api-user.json")
fire = firebase_admin.initialize_app(cred)

#Conexion a firestore DB = DataBase
db = firestore.client()

#Se crea la referencia de la base de datos
users_ref = db.collection("users/username")
#tasks_for_user = db.collection("username")

#Leer todos los usuarios
def leer_users( ):
    docs = users_ref.get()
    for user in docs:
        print(f"ID: {user.id} => DATA:{user.to_dict()}")

# --- Leer una solo el user ---
def leer_user( ):
    user = users_ref.document("id").get( )
    print(user.to_dict()) 
"""
# --- Leer una solo la tarea ---
def leer_user( ):
    task= users_ref.document("DL4G8jTB4Fax3XbJYahb").get( )
    print(task.to_dict()) """

# --- Crea el usuario ---
def crear_user(username, tarea):
    users_ref.document().set(username)
    users_ref.document().set(tarea)

new_user = {"username": "juan2001",
            }

new_task = {"name": "Juan Pablo", 
            "check": "Hacer tarea",
            "fecha": datetime.datetime.now()
            }         

crear_user(new_user, new_task)


