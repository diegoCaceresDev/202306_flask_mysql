"""Book controllers."""

# App
from app import app

# Flask
from flask import render_template, request, redirect, url_for, flash


@app.route("/")
def index():
    return render_template("books/books.html")
