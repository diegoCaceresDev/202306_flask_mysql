from app import app
from flask import render_template, redirect, request, flash

# Models
from app.models.usuarios import Usuario

@app.route("/")
# Renderiza todos los usuarios

def usuarios():
    usuarios = Usuario.get_all()
    return render_template("usuarios/usuarios.html", usuarios=usuarios)


@app.route("/usuarios/<id>/")
# Renderiza pagina que muestra un usuario por su ID

def show_user(id):
    
    data = {
        "id": int(id)
    }
    
    usuario = Usuario.get_one(data)
    
    print("Este es el usuario>", usuario)
    
    return render_template("usuarios/usuario.html", usuario=usuario)



@app.route("/add_user/")
# Renderiza pagina para agregar usuarios

def add_user():
    return render_template("usuarios/add_user.html")


@app.route("/edit_user/<id>/")
# Renderiza pagina para actualizar datos de usuarios
def edit_user(id):
    
    data = {
        "id": int(id)
    }
    
    usuario = Usuario.get_one(data)
    
    return render_template("usuarios/edit_user.html", usuario=usuario)


@app.route("/process_form_add/", methods=["POST"])
# Agrega un nuevo usuario

def process_form_add():
    print(request.form)
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    
    usuarios = Usuario.add_user(data)

    return redirect("/")






@app.route("/delete_user/<id>/")
# Elimina el usuario por su ID

def delete_user(id):
    
    data = {
        "id": int(id)
    }
    
    Usuario.delete_user(data)
    flash('El usuario fue eliminado correctamente')
    return redirect("/")


@app.route("/process_form_edit/", methods=["POST"])
# Formulario para actualizar datos

def process_form_edit():
    print(request.form)
    
    data = {
        "id": request.form['id'],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    
    usuarios = Usuario.updated_user(data)
    flash(f"El Usuario {data['id']} fue actualizado correctamente")
    
    return redirect("/")