"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, 
                  overview=overview, 
                  release_date=release_date, 
                  poster_path=poster_path)
    
    db.session.add(movie)
    db.session.commit()

    return movie


def return_all_movies():
    """Return all movies."""
    
    return Movie.query.all()



def create_rating(score, movie, user):
    """Create and return a new rating."""

    rating = Rating(score=score,
                    movie=movie,
                    user=user)

    db.session.add(rating)
    db.session.commit()

    return rating 