from app import app
from flask import render_template, redirect, request

# Models
from app.models.usuarios import Usuario

@app.route("/")
def usuarios():
    
    usuarios = Usuario.get_all()
    
    return render_template("usuarios/usuarios.html", usuarios=usuarios)

@app.route("/add_user/")
def add_user():
    return render_template("usuarios/add_user.html")

@app.route("/process_form/", methods=["POST"])
def process_form():
    print(request.form)
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    
    usuarios = Usuario.add_user(data)

    return redirect("/")