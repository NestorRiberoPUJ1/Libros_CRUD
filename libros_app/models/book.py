from libros_app.config.mysqlconnection import connectToMySQL
from libros_app.models.author import Author


class Book:

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.authors=[]

    @classmethod
    def muestraBooksAll(cls):
        query = "SELECT books.* FROM esquema_libros.books;"
        results = connectToMySQL("esquema_libros").query_db(query)
        books = []
        for u in results:
            books.append(cls(u))
        return books

    @classmethod
    def createBook(cls, form):
        query = "INSERT INTO esquema_libros.books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s)"
        result = connectToMySQL("esquema_libros").query_db(query, form)
        return result

    @classmethod
    def cargaAuthor(cls,form):
        query = "SELECT * FROM esquema_libros.books WHERE books.id = %(id)s ;"
        result = connectToMySQL("esquema_libros").query_db(query,form)
        book = result[0]
        book = cls(book)
        form={"id":book.id}
        book.books=Author.muestraAuthor(form)
        return book

    @classmethod
    def muestraBooks(cls, form):
        query = "SELECT books.* FROM esquema_libros.books LEFT JOIN favorites ON books.id =favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE authors.id = %(id)s;"
        results = connectToMySQL("esquema_libros").query_db(query, form)
        books = []
        for u in results:
            books.append(cls(u))
        return books