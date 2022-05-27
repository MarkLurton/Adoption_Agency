from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Model. Has values name (text, required), species(text, required),
    photo_url (text, optional), age (int, optional), notes (text, optional), available (bool, required, defaults to true)"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCU8G7_gCnP8E2bMZbNKtOMOo2mQKxFTGBAqQIyqAgxIPEJjH8YdNpfUNW-ldCCOZiSoc&usqp=CAU')
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True, nullable=False)

