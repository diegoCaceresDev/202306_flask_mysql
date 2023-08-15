# App
from app import app 

#Controllers

from app.controllers import dojos
from app.controllers import ninjas


if __name__ == "__main__":
    app.run(debug=True)
