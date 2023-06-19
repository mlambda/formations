from flask import render_template
from tinydb import  where

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = TinyDB("python_flask_formation/db.json")

@app.route("/genre/<genre>")
def view_genres(genre):
    genres = db.table("genres").all()
    current_genre = db.table("genres").search(
        where("id") == genre)[0]
    artists_by_genre = db.table("artists").search(
        where("genreId") == genre)
    return render_template(
        "index.html",
        genres=genres,
        current_genre=current_genre,
        artists=artists_by_genre,
    )
