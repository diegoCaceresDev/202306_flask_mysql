#Config
from app import app
from flask import render_template, redirect, request, flash

#Models
from app.models.dojos import Dojo

@app.route("/dojos/")
def dojos():
    
    dojos = Dojo.get_all()
    
    return render_template("dojos/dojos.html", dojos=dojos)


@app.route("/dojos/add", methods=["POST"])
def add_dojo():
    
    data = {
        "name": request.form['name']
    }
    
    Dojo.add_dojo(data)
    
    return redirect("/dojos/")
    


@app.route("/dojos/<id>/")
def get_dojo(id:int):
    
    dojo= Dojo.get_one(id)
    
    return render_template("dojos/dojo.html", dojo=dojo)

