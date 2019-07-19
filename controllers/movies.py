from app.models import Movie, Imdb
from app import app
from flask import jsonify


@app.route('/movies')
def get_movies():
    bttf = Movie.objects.all()
    return jsonify({"movies": bttf})

@app.route('/movies', methods=['POST'])
def creat_movie():
    bttf = Movie(title="Back To The Future", year=1985)
    bttf.actors = [
        "Michael J. Fox",
        "Christopher Lloyd"
    ]
    bttf.imdb = Imdb(imdb_id="tt0088763", rating=8.5)
    bttf.save()
    return "created"
