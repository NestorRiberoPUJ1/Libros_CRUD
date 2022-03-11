from libros_app import app
from libros_app.controllers import author
from libros_app.controllers import book

if(__name__=="__main__"):
    app.run(debug=True)