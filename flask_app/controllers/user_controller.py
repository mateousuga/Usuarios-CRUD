#importar Flask
from flask import Flask, render_template, request, redirect

#importamos la app
from flask_app import app

#importamos los modelos a tuilizar
from flask_app.models.users import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    User.save(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    formulario = {"id": id} #diccionario que tiene el indicardor del usuario que queremos eliminar
    User.delete(formulario)
    return redirect('/')

@app.route('/edit/<int:id>') #despliega el formulario
def edit(id):
    #0btener la instancia del usuario
    formulario = {"id": id}
    user = User.get_by_id(formulario)
    return render_template('edit.html', user=user)

@app.route('/update', methods=['POST']) #guarda el formulario
def update():
    User.update(request.form)
    return redirect('/')