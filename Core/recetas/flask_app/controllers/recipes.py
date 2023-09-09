from flask import render_template, flash, redirect, session, request
from flask_app import app
from flask_app.models.recipes import Recipe



@app.route('/')
def inicio():

    if 'usuario' not in session:
        flash("Debes iniciar sesion", "error")
        return redirect("/login")


    return redirect("/recipes/")

@app.route('/recipes/')
def recipes():

    if 'usuario' not in session:
        flash("Debes iniciar sesion", "error")
        return redirect("/login")

    recipes = Recipe.get_all()
    return render_template('dashboard/inicio.html', recipes=recipes)

@app.route('/new_recipe/')
def recipe():
    
    return render_template("/dashboard/new_recipe.html")


@app.route('/add_recipe/', methods=["post"])
def add_recipe():
    
    errores = Recipe.validar(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/login")
        
    data= {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30_minutos': request.form['under_30_minutos'],
        'created_at': request.form['created_at'],
        'user_id': session['usuario']['id'],
    }
    
    Recipe.save(data)
    
    return redirect('/')


@app.route('/recipes/<int:id>')
def recipe_by_id(id):
    
    recipe = Recipe.get_by_id(id)
    
    return render_template("/dashboard/show.html", recipe = recipe)


@app.route('/recipes/delete/<int:id>')
def delete_by_id(id):
    
    Recipe.delete(id)
    flash("El recipe fue eliminado correctamente", "error")

    return redirect("/")


@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    
    recipe = Recipe.get_by_id(id)
    
    return render_template("dashboard/edit_recipe.html", recipe = recipe)


@app.route('/edit/<id>', methods=["post"])
def edit_by_id(id):
    
    errores = Recipe.validar(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/login")
        
    
    data= {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30_minutos': request.form['under_30_minutos'],
        'created_at': request.form['created_at'],
        'user_id': session['usuario']['id'],
    }
    
    Recipe.update(data)
    
    flash(data['name'] + " fue actualizado correctamente", "success")
    return redirect("/recipes/")    
