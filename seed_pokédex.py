from app import db
from models.pokédex_model import Pokédex
from models.pokémon_model import Pokémon
import click

from flask.cli import with_appcontext

import requests

@click.command(name='seed_pokedex')
@with_appcontext
def seed_pokedex():
    Pokémon.query.delete() # if you already have pokémon in your database, need to clear them first
    Pokédex.query.delete()
    id = range(1, 1011)
    for n in id:
      url = f"https://pokeapi.co/api/v2/pokemon/{n}/".format(id)
      response = requests.get(url)
      if response.status_code != 200:
        print(response.text)
        return
      else:
        data = response.json()
        pokédex_id = data['id']
        pokémon_name = data['species']['name']
        new_entry = Pokédex(id=pokédex_id, name=pokémon_name)
        db.session.add(new_entry)
        db.session.commit()
        ### Files below writes the desired data into another file
        ### Comment out if you do not want it to write. Uncomment to let it run.
        # log = open('pokédex_backup.py', 'a')
        # log.write(f"Pokédex(id='{pokédex_id}', name='{pokémon_name}')\n ")
        # log.close()