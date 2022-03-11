from libros_app.config.mysqlconnection import connectToMySQL


class Favorites:

    def __init__(self,data):
        self.book_id = data["book_id"]
        self.author_id = data["author_id"]
    
    @classmethod
    def updateFav(cls,form):
        query = "INSERT INTO esquema_libros.favorites (book_id,author_id) VALUES (%(book_id)s,%(author_id)s)"
        result = connectToMySQL("esquema_libros").query_db(query,form)
        return result