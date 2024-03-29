"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app. Called in app.py"""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model for pets"""

    __tablename__ = 'pets'

    __table_args__ = (CheckConstraint("age in ('baby', 'young', 'adult', 'senior')"),
                      # add a constraint for checking species
                      )

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

    species = db.Column(
        db.Text,
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False,
        default=''
    )

    age = db.Column(
        db.Text,
    )

    notes = db.Column(
        db.Text,
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )