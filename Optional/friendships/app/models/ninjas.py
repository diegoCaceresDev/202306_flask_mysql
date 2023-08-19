# Config
from app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data) -> None:
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def add_ninja(cls, data):
        """
        Agrega un nuevo Ninja
        """

        query = """
        INSERT INTO ninjas (`first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, now(), now(), %(dojo_id)s);"""

        return connectToMySQL("esquema_dojos_y_ninjas_uno_muchos").query_db(query, data)
