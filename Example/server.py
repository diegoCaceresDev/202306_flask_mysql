"""Configuración del servidor."""

# App
from app import app

# Controllers
from app.controllers.authors import *
from app.controllers.books import *



# Run
if __name__ == "__main__":
    app.run(debug=True, port=5001)
