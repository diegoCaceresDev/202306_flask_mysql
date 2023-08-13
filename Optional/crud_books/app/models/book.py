"""Book model."""

# Config
from app.config.mysql_connection import connectToMySQL


class Book:
    """Modelo de clase `Book`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `Book`."""

        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
