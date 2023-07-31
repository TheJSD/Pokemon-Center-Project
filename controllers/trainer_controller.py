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

@trainers_blueprint.route("/trainers/new")
def register_trainer_page():
    nurses = Nurse.query.all()
    return render_template("trainers/new_trainer.jinja", nurses=nurses)

@trainers_blueprint.route("/trainers", methods=["post"])
def add_trainer():
    name = request.form['name']
    contact = request.form['contact']
    nurse = request.form['nurse']
    if nurse == "None":
        nurse = None
    new_trainer = Trainer(name=name, contact=contact, nurse=nurse)
    db.session.add(new_trainer)
    db.session.commit()
    return redirect("/trainers")