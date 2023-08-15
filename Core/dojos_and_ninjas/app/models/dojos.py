# Config
from app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod 
    def get_all(cls):
        """
        Obtener datos de dojos
        """
        query = """SELECT * FROM esquema_dojos_y_ninjas_uno_muchos.dojos;"""
        results = connectToMySQL("esquema_dojos_y_ninjas_uno_muchos").query_db(query)
        dojos:list = []
        
        for dojo in results:
            dojos.append(cls(dojo))
            
        return dojos
    
    
    @classmethod
    def add_dojo(cls, data):
        """
        Agrega un nuevo DOJO
        """
        
        query = """
        INSERT INTO dojos (`name`, `created_at`, `updated_at`) 
        VALUES (%(name)s, now(), now());"""

        return connectToMySQL("esquema_dojos_y_ninjas_uno_muchos").query_db(query, data)
    
    
    @classmethod 
    def get_one(cls, id):
        """
        Obtener datos de un Dojo por su ID
        """
        query = """  SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"""
        data = {
            "id": id
        }
        results = connectToMySQL("esquema_dojos_y_ninjas_uno_muchos").query_db(query, data)
        
        print(results[0]['name'])
        
        return (results)
    
