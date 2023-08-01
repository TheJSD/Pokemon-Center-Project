from app import db
from models.pokédex_model import Pokédex
import click

from flask.cli import with_appcontext

import requests

@click.command(name='seed_pokedex')
@with_appcontext
def seed_pokedex():
    Pokédex.query.delete()
    id = range(1, 1011)
    for n in id:
      url = f"https://pokeapi.co/api/v2/pokemon/{n}/".format(id)
      response = requests.get(url)
      if response.status_code != 200:
        print(response.text)
      else:
        data = response.json()
        new_entry = Pokédex(id=data['id'], name=data['species']['name'])
        db.session.add(new_entry)
        db.session.commit()
        ### Files below writes the desired data into another file
        ### Comment out if you do not want it to write
        # log = open('pokédex_backup.py', 'a')
        # log.write(f"pokédexentry{data['id']} = Pokédex(id='{data['id']}', name='{data['species']['name']}')\n")
        # log.close()