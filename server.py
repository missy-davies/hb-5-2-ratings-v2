"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined 

@app.route('/')
def show_homepage():
    """Return homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def show_movies():
    """Show all movies."""

    movies = crud.return_all_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """Show more detailed information on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)


@app.route('/users')
def show_users():
    """Show all users."""

    users = crud.return_all_users()

    return render_template('all_users.html', users=users)


@app.route('/user-login', methods=['POST'])
def log_user_in():
    """Logs user into their account."""

    user = crud.get_user_by_email(request.form['email'])

    password = request.form['password']

    if user == None:
        flash('''An account for this email doesn't exist yet. 
                Please create a new account''')
    elif password != user.password:
        flash('Wrong password. Please try again.')
    else:
        flash('Logged in!')
        session['user-id'] = user.user_id

    return redirect('/')

@app.route('/users', methods=['POST'])
def register_new_user():
    """Registers a new user"""

    existing_user = crud.get_user_by_email(request.form['email'])

    if existing_user == None:

        crud.create_user(request.form['email'], request.form['password'])
        flash('You have successfully created an account. You can log in.')

    else:
        flash('An account already exists with this email. Please try again.')

    return redirect('/')


@app.route('/users/<user_id>')
def show_user_details(user_id):
    """Show more detailed information on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
