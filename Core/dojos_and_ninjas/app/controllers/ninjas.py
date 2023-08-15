from app import app
from flask import render_template, redirect, request, flash

#Models
from app.models.ninjas import Ninja
from app.models.dojos import Dojo


@app.route("/ninjas/")
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninjas/ninjas.html", dojos= dojos)



@app.route("/ninjas/add/", methods=["POST"])
def add_ninja():
    
    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }
    
    Ninja.add_ninja(data)
    
    return redirect("/ninjas/")
