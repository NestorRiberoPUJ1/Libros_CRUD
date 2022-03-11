from flask import Flask, render_template, request, redirect
from libros_app import app
from libros_app.models import author
from libros_app.models import book 
from libros_app.models.favorites import Favorites

@app.route("/")
def root():
    return redirect("/authors")

@app.route("/authors")
def authors():
    authors =  author.Author.muestraAuthorsAll()
    return render_template("new_author.html",authors=authors)

@app.route("/create",methods=["POST"])
def create():
    print(request.form)
    if(request.form["type"]=="authors"):
        author.Author.createAuthor(request.form)
        return redirect("/authors")
    elif(request.form["type"]=="books"):
        book.Book.createBook(request.form)
        return redirect("/books")
    elif(request.form["type"]=="add_author_book"):
        Favorites.updateFav(request.form)
        id=int(request.form["author_id"])
        return redirect(f"/author/{id}")
    elif(request.form["type"]=="add_book_author"):
        Favorites.updateFav(request.form)
        id=int(request.form["book_id"])
        return redirect(f"/book/{id}")

@app.route("/author/<int:id>")
def viewAuthor(id):
    form={"id":id}
    authore=author.Author.cargaAuthor(form)
    books=book.Book.muestraBooksAll()
    return render_template("view_author.html",author=authore,books=books)