from libros_app.config.mysqlconnection import connectToMySQL
from libros_app.models import book

class Author:

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.books=[]

    @classmethod
    def muestraAuthorsAll(cls):
        query = "SELECT * FROM esquema_libros.authors;"
        results = connectToMySQL("esquema_libros").query_db(query)
        author = []
        for u in results:
            author.append(cls(u))
        return author

    @classmethod
    def createAuthor(cls,form):
        query = "INSERT INTO esquema_libros.authors (name) VALUES (%(name)s)"
        result = connectToMySQL("esquema_libros").query_db(query,form)
        return result

    @classmethod
    def cargaAuthor(cls,form):
        query = "SELECT * FROM esquema_libros.authors WHERE authors.id = %(id)s ;"
        result = connectToMySQL("esquema_libros").query_db(query,form)
        author = result[0]
        author = cls(author)
        form={"id":author.id}
        author.books=book.Book.muestraBooks(form)
        return author

    @classmethod
    def muestraAuthor(cls, form):
        query = "SELECT authors.* FROM esquema_libros.books LEFT JOIN favorites ON books.id =favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL("esquema_libros").query_db(query, form)
        books = []
        for u in results:
            books.append(cls(u))
        return books
