"""Author controllers."""

# App
from app import app

# Flask
from flask import render_template, request, redirect, url_for, flash

# Models
from app.models.author import Author


@app.route("/authors/")
def authors():
    """
    Listar todos los autores y mostrar el formulario.
    """

    authors = Author.get_all()
    return render_template("authors/authors.html", authors=authors)


@app.route("/author/<int:id>/")
def author(id):
    """
    Mostrar un autor con sus libros favoritos.
    """
    data = {"id": id}
    author = Author.get_one(data)
    return render_template("authors/author.html", author=author)
