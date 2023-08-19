# App
from app import app 

#Controllers

from app.controllers import friendships

if __name__ == "__main__":
    app.run(debug=True)
