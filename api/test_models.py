from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# Tester la récupération de quelques films

movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")


# Récupérer des films du genre Action
action_movies = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()

for movie in action_movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genre : {movie.genres}")


# tester la récupération de quelques évaluations (ratings)

Ratings = db.query(Rating).limit(20).all()

for rating in Ratings:
    print(
        f"UserID : {rating.userId}, MovieID : {rating.movieId}, Rating : {rating.rating}"
    )

# Récupérer films dont note > 4 :
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
)

for title, rating in high_rated_movies:
    print(title, rating)

# Récupérer les tags associés aux films

tags = db.query(Tag.userId, Tag.tag, Movie.title).join(Movie).limit(5).all()

for userId, tag, title in tags:
    print(f"UserID : {userId}, Tag : {tag}, Title : {title}")


# Tester la classe link

links = db.query(Link).limit(5).all()

for link in links:
    print(f"Movie ID : {link.movieId}, Link : {link.imdbId}, IMG : {link.tmdbId}")

# Fermer la session
db.close()
