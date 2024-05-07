
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import db, credentials

app = Flask(__name__) #Instanciando o objeto Flask
from app import routes
#Para trabalhar com o flash preciso definir uma secret key, uma chave de acesso
app.config['SECRET_KEY'] = "123"

#Inicializando o banco de Dados
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://crudflask-d546e-default-rtdb.firebaseio.com/"})

"""
#creating a reference to root mode
ref = db.reference('/')

#buscando dados do bd
ref.get()

#Consultando
db.reference("/name").get()
#alterando
db.reference("/videos").set(3)
ref.get()

#Atualizando
db.reference("/").update({"language":"python"})
ref.get()

#Inserindo dados no BD
db.reference("/titles").push().set("Criação de BD em Python")
ref.get()

#Mudança de dados - Transação
def increment_transaction(current_val):
    return current_val + 1

db.reference("/title_count").transaction("increment_transaction")
ref.get()

db.reference("language").delete()
ref.get()
"""






