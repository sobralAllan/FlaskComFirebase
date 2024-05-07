from app import app
from flask import render_template
from flask import flash
from flask import redirect
from flask import Flask, request, jsonify
from firebase_admin import db, credentials
import this
this.id = 0
#Configuração de Banco de Dados em Flask: https://medium.com/google-cloud/building-a-flask-python-crud-api-with-cloud-firestore-firebase-and-deploying-on-cloud-run-29a10c502877
@app.route('/', defaults={"nome":"usuário"}) #Definindo a raiz do projeto
@app.route('/index', defaults={"nome":"usuário"}) #Quando não quero passar nenhum nome como parâmetro
@app.route('/index/<nome>')
def index(nome):
    dados = {"profissao":"Professor", "area":"T.I."}
    return render_template('index.html', nome=nome, dados=dados, titulo="Página Principal")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get("usuario")
    senha   = request.form.get("senha")
    if usuario == "admin" and senha == "senha":
        usuario = db.reference("/cadastrar").get()
        senha = db.reference("/cadastrar").get()
        return f"Usuário: {usuario}\n Senha: {senha}"
    else:
        flash("Dados Inválidos!") #Array de mensagens
        flash("Login e/ou senha errados!")
        this.id+= 1

        #Parei aqui, meditar sobre...
        db.reference("/cadastrar").push('usuarios').set([this.id,usuario, senha])
        return redirect('/login')

#
"""
#Comandos do banco de dados
@app.route('/add', methods=['POST'])
def create():
   
        #create() : Add document to Firestore collection with request body
        #Ensure you pass a custom ID as part of json body in post request
        #e.g. json={'id': '1', 'title': 'Write a blog post'}
    
    json = {'usuario':'teste','senha':'123'}
    try:
        id = request.json['id']
        todo_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/list', methods=['GET'])
def read():
    
        #read() : Fetches documents from Firestore collection as JSON
        #todo : Return document that matches query ID
        #all_todos : Return all documents
    
    try:
        # Check if ID was passed to URL query
        todo_id = request.args.get('id')
        if todo_id:
            todo = todo_ref.document(todo_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_todos = [doc.to_dict() for doc in todo_ref.stream()]
            return jsonify(all_todos), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/update', methods=['POST', 'PUT'])
def update():
    
        #update() : Update document in Firestore collection with request body
        #Ensure you pass a custom ID as part of json body in post request
        #e.g. json={'id': '1', 'title': 'Write a blog post today'}
    
    try:
        id = request.json['id']
        todo_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
   
        #delete() : Delete a document from Firestore collection
    
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        todo_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

"""