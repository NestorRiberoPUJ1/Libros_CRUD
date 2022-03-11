from flask import Flask, render_template, request, redirect
from libros_app import app
from libros_app.models.author import Author
from libros_app.models.book import Book


@app.route("/books")
def books():
    books = Book.muestraBooksAll()
    print(books)
    return render_template("new_book.html", books=books)


