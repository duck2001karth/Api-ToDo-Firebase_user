import email
import re
from urllib import response
from certifi import contents
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime, requests

#Configuraciones para firebase
cred = credentials.Certificate("acount_key_api-user.json")
fire = firebase_admin.initialize_app(cred)

#Conexion a firestore DB = DataBase
db = firestore.client()

#Se crea la referencia de la base de datos
users_ref = db.collection("users")
#Api web
API_KEY = "AIzaSyCdtDzFbbJEfJx9A4YPZX9WgQmvJHrZewA"

def login(email, password):
    credentials = {"email":email,"password":password,"returnSecureToken":True}
    response = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}".format(API_KEY),data=credentials)
    if response.status_code == 200:
       #print(response.content)
       
       content = response.content
       llave = response.json().keys()
       print(llave["localId"])
       



    elif response.status_code == 400:
        print(response.content)    


    return response.content
    #print(response.status_code)
    #print(response.content)

#Leer todos los usuarios
def get_ref_user(id):
    user_ref = users_ref.document(id)
    user = user_ref.get()
    if user.exists:
        print(user.to_dict()) 
        docs_ref = user_ref.collection("tasks")
    else:
        print("Usuario no existe")    
        docs_ref = False
    return docs_ref


    """docs = docs_ref.get()
    for doc in docs:
        print(f"ID:{doc.id} => DATA:{doc.to_dict()}")"""

#-------------------------------------------------------------------
#Leer todo los tasks
def leer_tasks(ref):
    #docs = tasks_ref.stream( )
    docs = ref.get()
    for task in docs:
        print(f"ID:{task.id} => DATA:{task.to_dict()}")
#-------------------------------------------------------------------
#Leer una sola task
def leer_task(ref, id):
    task = ref.document(id).get()
    print(task.to_dict())
#-------------------------------------------------------------------
#Crear tarea (task)
def crear_task(ref, task):
    new_task = {"name":task,
                "check":False,
                "fecha": datetime.datetime.now()}
    ref.document().set(new_task)            
#-------------------------------------------------------------------
#Actualizar tarea (task)
def actualizar_task(ref, id):
    ref.document(id).update({"Check":True})

#-------------------------------------------------------------------
#Eliminar tarea (task)
def eliminar_task(ref, id):
    resp = ref.document(id).delete()
    print(resp)

#-------------------------------------------------------------------
#Completar tarea
def completar_task(ref):
    completed = ref.where("check", "==", False).get()
    for task in completed:
        print(f"ID:{task.id} => DATA:{task.to_dict()}")

#-------------------------------------------------------------------
#create_task(users_ref)
#name_task = input("\n Ingresa el nombre de la tarea: ")
#create_task(name_task)
#update_task("paiwIA05qT51TIS1NAXO")       
#delete_task("paiwIA05qT51TIS1NAXO")     

#get_task_completed()
#-------------------------------------------------------------------
#login and passoword
email = input("Ingrese el email (correo electronico): ")
password = input("Ingrese el password (contraseña): ")
login(email, password)
#-------------------------------------------------------------------
#Mostrar la info en el terminal y verificar
#Si la ID esta diferente mostrara un mensaje que no existe tal "ID"
#ref_user = get_ref_user("o5nHOYosJnBY0Ihkm8Im")
#if ref_user:
#  crear_task(ref_user,"Comprobar la validación")
#-------------------------------------------------------------------
#Mostrar la informacion en el terminal
#leer_tasks(ref_user) 
#-------------------------------------------------------------------
#leer_task(ref_user, "akkxmGKAW3hPnLxKzjMS")
#-------------------------------------------------------------------
#Crear la tarea en el usuario que esta referenciado con en el ID
##crear_task(ref_user, "Realizar la tarea")
