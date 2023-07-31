from flask import Flask, Blueprint, render_template, request, redirect
from models.pokémon_model import Pokémon, empty_returns_null
from models.nurse_model import Nurse
from models.trainer_model import Trainer
from app import db

trainers_blueprint = Blueprint("trainers", __name__)

@trainers_blueprint.route("/trainers")
def trainers():
    trainers = Trainer.query.all()
    return render_template("trainers/index.jinja", trainers=trainers)

@trainers_blueprint.route("/trainers/<id>")
def show_trainer(id):
    trainer = Trainer.query.get(id)
    nurse = Nurse.query.get(trainer.nurse)
    nurse = empty_returns_null(nurse)
    assigned_pokémon = Pokémon.query.filter_by(trainer = id)
    assigned_pokémon = empty_returns_null(assigned_pokémon)
    return render_template("/trainers/show_trainer.jinja", trainer = trainer, nurse=nurse, assigned_pokémon=assigned_pokémon)