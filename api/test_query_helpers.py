from database import SessionLocal
from query_helpers import *

db = SessionLocal()

movie = get_movie(db, movie_id=1)
print(movie.title, movie.genres)

movies = get_movies(db, limit=5)
for film in movies:
    print(f"ID : {film.movieId}, Titre : {film.title}, genres : {film.genres}")


rating = get_rating(db, user_id=1, movie_id=1)
print(
    f"Movie ID : {rating.movieId}, userID : {rating.userId}, rating : {rating.rating} "
)

ratings = get_ratings(db, min_rating=3.5, limit=10, user_id=3)
for film in ratings:
    print(f"ID : {film.movieId}, rating : {film.rating}")


tag = get_tag(db, user_id=2, movie_id=60756, tag_text="funny")
print(tag)
print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}")

tags = get_tags(db, skip=0, limit=5)
for film in tags:
    print(
        f"GET_TAGS : Movie ID : {film.movieId}, userID : {film.userId}, tag : {film.tag}"
    )

link = get_link(db, movie_id=1)
print(link)
print(f"MovieID = {link.movieId}, link : {link.imdbId}")

links = get_links(db, skip=1, limit=100)
for film in links:
    print(f"LINKS - Movie ID : {film.movieId}, Lien : {film.imdbId} - {film.tmdbId}")

n_movies = get_movie_count(db)
print(n_movies)

n_links = get_link_count(db)
print(f"Nombre de liens : {n_links}")

# Fermer la session
db.close()
