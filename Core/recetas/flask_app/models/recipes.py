import os

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.usuarios import Usuario

class Recipe:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_minutos = data['under_30_minutos']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']



    @classmethod
    def validar(cls, formulario):
        """
        Valida si los datos recibidos por el usuario son correctos
        """
        errores = []

        if len(formulario['name']) < 3:
            errores.append(
                "El titulo debe tener al menos 3 caracteres"
            )

        if len(formulario['instructions']) < 3:
            errores.append(
                "El Network debe tener al menos 3 caracteres"
            )
            
        if len(formulario['description']) < 3:
            errores.append(
                "La descripcion debe tener al menos 3 caracteres"
            )

        return errores


    @classmethod
    def get_all(cls):
        """
        Obtiene todos los datos de las recipes con el usuario que creo la misma
        """
        resultados_instancias = []
        query = "SELECT r.id,name,under_30_minutos,first_name,last_name,user_id FROM recipes r LEFT JOIN users ON user_id = users.id;"
        resultados = connectToMySQL(os.getenv('BASE_DATOS')).query_db(query)
        for resultado in resultados:
            resultados_instancias.append(resultado)

        
        return resultados_instancias
    
    
    @classmethod
    def save(cls, data ):
        """
        Guarda un nuevo show en la base de datos
        """
        print(data)
        query = """INSERT INTO recipes (`name`, `description`, `instructions`, `under_30_minutos`, `user_id`, `created_at`, `updated_at`) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30_minutos)s, %(user_id)s, %(created_at)s, now());"""
        return connectToMySQL(os.getenv('BASE_DATOS')).query_db( query, data )


    @classmethod
    def get_by_id(cls, id ):
        """
        Obtener todos los datos de un recipe a traves de su 'ID'
        """
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id  WHERE recipes.id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL(os.getenv('BASE_DATOS')).query_db( query, data )
        
        return resultados[0]
    
    
    @classmethod
    def delete(cls, id ):
        """
        Elimina todos los datos de un recipe a traves de su 'ID'
        """
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL(os.getenv('BASE_DATOS')).query_db( query, data )
        return True
    
    
    @classmethod
    def update(cls, data ):
        """
        Actualiza todos los datos de un recipe a traves de su 'ID'
        """
        query = "UPDATE recipes SET `title` = %(title)s, `network` = %(network)s, `description` = %(description)s, `released_date` = %(released_date)s WHERE (`id` = %(id)s);"

        connectToMySQL(os.getenv('BASE_DATOS')).query_db( query, data )
        return True
    
