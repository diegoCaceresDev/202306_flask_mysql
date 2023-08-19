# Config
from app.config.mysqlconnection import connectToMySQL

class User():
    def __init__(self,data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod 
    def get_all_friendships(cls):
        """
        Obtener datos de Users y Friendships
        """
        query = """SELECT * FROM users a 
        LEFT JOIN friendships f ON a.id = f.user_id 
        LEFT JOIN users b on b.id = f.friend_id """
        results = connectToMySQL("friendships").query_db(query)
        friendships:list = []
        
        for user in results:
            friendships.append(user)
        
        return friendships
    
    @classmethod 
    def get_all_users(cls):
        """
        Obtener datos de Users 
        """
        query = """SELECT * FROM users"""
        results = connectToMySQL("friendships").query_db(query)
        users:list = []
        
        for user in results:
            users.append(cls(user))
        
        return users
    
    @classmethod
    def add_user(cls, data):
        """
        Agrega un nuevo User
        """
        
        query = """
        INSERT INTO users (first_name, last_name, created_at , updated_at) 
        VALUES (%(first_name)s, %(last_name)s, now(), now());"""

        return connectToMySQL("friendships").query_db(query, data)
    
    @classmethod
    def create_friendship(cls, data: dict):
        """
        Crea un nuevo friendship
        """
        
        query = """
        INSERT INTO friendships (user_id, friend_id, created_at , updated_at) 
        VALUES (%(user_id)s, %(friend_id)s, now(), now());"""

        return connectToMySQL("friendships").query_db(query, data)
    

    
    