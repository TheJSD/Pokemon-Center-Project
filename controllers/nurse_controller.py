from flask import Flask, Blueprint, render_template
from models.pokémon_model import Pokémon
from models.nurse_model import Nurse
from app import db

nurses_blueprint=Blueprint("nurses", __name__)

@nurses_blueprint.route("/nurses")
def nurses():
    nurses = Nurse.query.all()
    return render_template("nurses/index.jinja", nurses=nurses)