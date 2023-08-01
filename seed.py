from app import db
from models.nurse_model import Nurse
from models.pokémon_model import Pokémon
from models.trainer_model import Trainer
from models.pokédex_model import Pokédex
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Trainer.query.delete()
    Pokémon.query.delete()
    Nurse.query.delete()
    nurse1=Nurse(name="Nurse Joy 1")
    nurse2=Nurse(name="Nurse Joy 2")
    nurse3=Nurse(name="Nurse Joy 3")
    nurse4=Nurse(name="Blissey")

    trainer1=Trainer(name="Ash", contact="ashketchum@pokemail.com")
    trainer2=Trainer(name="Brock", contact="brock@pewtergym.com")
    trainer3=Trainer(name="Misty", contact="misty@ceruleangym.com")
    trainer4=Trainer(name="Liam", contact="camperliam@pewtergym.com")

    db.session.add(trainer1)
    db.session.add(trainer2)
    db.session.add(trainer3)
    db.session.add(trainer4)
    db.session.commit()

    pokémon1=Pokémon(species="25", trainer=trainer1.id, dob="12/9/1998")
    pokémon2=Pokémon(species="95", trainer=trainer2.id)
    pokémon3=Pokémon(species="120", trainer=trainer3.id)
    pokémon4=Pokémon(species="74", nickname="Rocky", trainer=trainer4.id)

    db.session.add(nurse1)
    db.session.add(nurse2)
    db.session.add(nurse3)
    db.session.add(nurse4)


    db.session.add(pokémon1)
    db.session.add(pokémon2)
    db.session.add(pokémon3)
    db.session.add(pokémon4)

    db.session.commit()