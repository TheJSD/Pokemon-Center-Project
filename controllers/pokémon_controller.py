from flask import Flask, Blueprint, render_template
from models.pokémon_model import Pokémon
from app import db

pokémon_blueprint = Blueprint("pokémon", __name__)

@pokémon_blueprint.route("/pokémon")
def pokémon():
    pokémon = Pokémon.query.all()
    return render_template("pokémon/index.jinja", pokémon=pokémon)