# Config
from app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        """
        Obtener datos de usuarios
        """
        
        query = """SELECT * FROM users;"""
        results = connectToMySQL("users_schema").query_db(query)
        users:list = []
        
        for user in results:
            users.append(cls(user))

        return users
    
    @classmethod
    def add_user(cls, data):
        """
        Agrega un nuevo usuario
        """
        
        query = """
        INSERT INTO users (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, now(), now());"""
        usuarios = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "email": data["email"]
        }

        return connectToMySQL("users_schema").query_db(query, data)
        

    
    
