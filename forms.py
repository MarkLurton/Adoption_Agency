from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, URL


class PetForm(FlaskForm):
    """Add Pet Form"""
    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name cannot be blank")])
    species = SelectField("Pet Species", validators=[InputRequired(message="Pet Species cannot be blank")], choices=[('dog', 'dog'), ('cat', 'cat'), ('porcupine', 'porcupine')])
    photo_url = StringField("Pet Photo URL", validators=[Optional(), URL("Photo must be submitted in URL format")])
    age = IntegerField("Pet Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Pet is Available")
