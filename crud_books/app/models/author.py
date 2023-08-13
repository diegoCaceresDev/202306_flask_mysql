"""Author model."""

# Config
from app.config.mysql_connection import connectToMySQL

# Models
from app.models.book import Book


class Author:
    """Modelo de clase `Author`."""

    def __init__(self, data: dict) -> None:
        """Constructor de la clase `Author`."""

        self.id = data["id"]
        self.name = data["name"]
        self.favorite_books = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Obtener todos los autores.
        """

        query = """SELECT * FROM authors;"""
        results = connectToMySQL("crud_books_schema").query_db(query)
        authors: list = []

        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one(cls, data: dict):
        """
        Obtener un autor por su id.
        """

        query = """
        SELECT * FROM authors
        LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON books.id = favorites.book_id
        WHERE authors.id = %(id)s;
        """
        result = connectToMySQL("crud_books_schema").query_db(query, data)
        author = cls(result[0])

        for row in result:
            if row["book_id"] is not None:
                author.favorite_books.append(Book(row))
                
        # print(f"Author: {author.__dict__}")
        return author
