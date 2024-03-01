"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SelectField
from wtforms.validators import InputRequired


class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()])

    species = StringField(
        "Species",
        validators=[InputRequired()])

    photo_url = URLField(
        "Photo URL")

    age = SelectField(
        "Age",
        choices=[('baby', 'Baby'),
                 ('young', 'Young'),
                 ('adult', 'Adult'),
                 ('senior', 'Senior')],
        validators=[InputRequired()])

    notes = StringField("Notes")


