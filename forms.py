"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField, BooleanField
from wtforms.validators import InputRequired, AnyOf, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = SelectField(
        "Species",
        choices=[('dog', 'Dog'),
                 ('cat', 'Cat'),
                 ('porcupine', 'Porcupine')],
        validators=[InputRequired(),
                    AnyOf(['dog', 'cat', 'porcupine'])]
        )

    photo_url = URLField(
        "Photo URL", validators=[URL(), Optional()])

    age = SelectField(
        "Age",
        choices=[('baby', 'Baby'),
                 ('young', 'Young'),
                 ('adult', 'Adult'),
                 ('senior', 'Senior')],
        validators=[InputRequired(),
                    AnyOf(['baby', 'young', 'adult', 'senior'])])

    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet"""

    photo_url = URLField(
        "Photo URL", validators=[URL(), Optional()])

    notes = StringField("Notes")

    available = BooleanField('Available')