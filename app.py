"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def display_homepage():
    """Displays homepage"""

    pets = Pet.query.all()
    return render_template("homepage.html", pets = pets)



@app.route("/add", methods=['GET', 'POST'])
def add_pet():
    """Show user add pet form and handle adding of pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
        )

        db.session.add(new_pet)
        db.session.commit()

        flash("Pet added!")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)








