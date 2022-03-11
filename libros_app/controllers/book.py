from flask import Flask, render_template, request, redirect
from libros_app import app
from libros_app.models import author
from libros_app.models import book


@app.route("/books")
def books():
    books = book.Book.muestraBooksAll()
    print(books)
    return render_template("new_book.html", books=books)


@app.route("/book/<int:id>")
def viewBook(id):
    form = {"id": id}
    booke = book.Book.cargaBook(form)
    authors = author.Author.muestraAuthorsAll()
    return render_template("view_book.html", book=booke, authors=authors)
