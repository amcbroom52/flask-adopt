"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
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


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Handle showing and editing info about a pet"""

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash("Pet Updated")
        return redirect(f'/{pet_id}')

    else:
        return render_template('show_pet.html', form=form, pet=pet)








