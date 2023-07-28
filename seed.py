from app import db
from models.nurse_model import Nurse
from models.pokémon_model import Pokémon
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Nurse.query.delete()
    Pokémon.query.delete()
    nurse1=Nurse(name="Nurse Joy 1")
    nurse2=Nurse(name="Nurse Joy 2")
    nurse3=Nurse(name="Nurse Joy 3")
    nurse4=Nurse(name="Blissey")

    pokémon1=Pokémon(species="Pikachu", contact="ashketchum@pokemail.com", dob="12/9/1998")
    pokémon2=Pokémon(species="Onyx", contact="brock@pewtergym.com")
    pokémon3=Pokémon(species="Staryu", contact="misty@ceruleangym.com")
    pokémon4=Pokémon(species="Geodude", nickname="Rocky", contact="camperliam@pewtergym.com")

    db.session.add(nurse1)
    db.session.add(nurse2)
    db.session.add(nurse3)
    db.session.add(nurse4)

    db.session.add(pokémon1)
    db.session.add(pokémon2)
    db.session.add(pokémon3)
    db.session.add(pokémon4)

    db.session.commit()