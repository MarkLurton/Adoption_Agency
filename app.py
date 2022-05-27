from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'letsgostros'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def display_home_page():
    """Render home page"""

    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def display_add_pet_form():
    """Render pet form and submit to db"""

    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else None
        age = form.age.data if form.age.data else None
        notes = form.notes.data if form.notes.data else None
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        flash(f'{pet.name} successfully added!')

        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<pet_id>', methods=['GET', 'POST'])
def display_pet_info_page(pet_id):
    """Renders pet info and edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data if form.photo_url.data else "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCU8G7_gCnP8E2bMZbNKtOMOo2mQKxFTGBAqQIyqAgxIPEJjH8YdNpfUNW-ldCCOZiSoc&usqp=CAU"
        pet.age = form.age.data if form.age.data else None
        pet.notes = form.notes.data if form.notes.data else None
        pet.available = form.available.data


        db.session.add(pet)
        db.session.commit()

        flash(f'{pet.name} successfully edited!')

        return redirect(f'/{pet.id}')
    else:
        return render_template('pet_details.html', form=form, pet=pet)