from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

jimjim = Pet(name='JimJim', species='dog', age=8, available=True)
jj = Pet(name='JJ', species='dog', age=12, available=True)
farrah = Pet(name='Farrah', species='cat', age=7)
cj = Pet(name='CJ', species='cat', age= 10)

db.session.add(jimjim)
db.session.add(jj)
db.session.add(farrah)
db.session.add(cj)

db.session.commit()