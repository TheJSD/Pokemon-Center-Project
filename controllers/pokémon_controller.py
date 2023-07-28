from flask import Flask, Blueprint, render_template
from models.pokémon_model import Pokémon
from models.nurse_model import Nurse
from app import db

pokémon_blueprint = Blueprint("pokémon", __name__)

@pokémon_blueprint.route("/pokémon")
def pokémon():
    pokémon = Pokémon.query.all()
    return render_template("pokémon/index.jinja", pokémon=pokémon)

@pokémon_blueprint.route("/pokémon/<id>")
def show_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    return render_template("pokémon/show_pokémon.jinja", single_pokémon=single_pokémon)

@pokémon_blueprint.route("/pokémon/new_pokémon")
def add_pokémon():
    nurses = Nurse.query.all()
    return render_template("pokémon/new_pokémon.jinja", nurses=nurses)