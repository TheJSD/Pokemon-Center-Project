from flask import Flask, Blueprint, render_template, request, redirect
from models.pokémon_model import Pokémon, empty_returns_null
from models.nurse_model import Nurse
from models.trainer_model import Trainer
from models.pokédex_model import Pokédex, id_from_string
from app import db

pokémon_blueprint = Blueprint("pokémon", __name__)

@pokémon_blueprint.route("/pokémon")
def pokémon():
    pokémon = Pokémon.query.all()
    return render_template("pokémon/index.jinja", pokémon=pokémon, title="Pokémon")

@pokémon_blueprint.route("/pokémon/<id>")
def show_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    if single_pokémon.trainer != None:
        trainer = Trainer.query.get(single_pokémon.trainer)
        nurse = Nurse.query.get(trainer.nurse)
    else:
        trainer=None
        nurse=None
    return render_template("pokémon/show_pokémon.jinja", single_pokémon=single_pokémon, trainer=trainer, nurse=nurse)

@pokémon_blueprint.route("/pokémon/new_pokémon")
def register_pokémon_page():
    trainers = Trainer.query.filter(Trainer.nurse != None)
    pokédex = Pokédex.query.all()
    return render_template("pokémon/new_pokémon.jinja", trainers=trainers, pokédex=pokédex)

@pokémon_blueprint.route("/pokémon", methods=["post"])
def add_pokemon():
    species=request.form['species']
    species=id_from_string(species)
    nickname=request.form['nickname']
    dob=request.form['date_of_birth']
    treatment_notes=request.form['treatment_notes']
    trainer=request.form['trainer']
    nickname = empty_returns_null(nickname)
    dob = empty_returns_null(dob)
    treatment_notes = empty_returns_null(treatment_notes)
    new_pokémon = Pokémon(species=species,
                    nickname=nickname,
                    dob=dob,
                    trainer=trainer,
                    treatment_notes=treatment_notes)
    db.session.add(new_pokémon)
    db.session.commit()
    return redirect ("/pokémon")

@pokémon_blueprint.route("/pokémon/<id>/edit")
def edit_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    trainers = Trainer.query.all()
    pokédex = Pokédex.query.all()
    return render_template("pokémon/edit_pokémon.jinja", single_pokémon=single_pokémon, trainers=trainers, pokédex=pokédex)

@pokémon_blueprint.route("/pokémon/<id>", methods=["post"])
def update_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    species=request.form['species']
    species=id_from_string(species)
    nickname=request.form['nickname']
    dob=request.form['date_of_birth']
    treatment_notes=request.form['treatment_notes']
    trainer=request.form['trainer']
    nickname = empty_returns_null(nickname)
    dob = empty_returns_null(dob)
    treatment_notes = empty_returns_null(treatment_notes)
    single_pokémon.species=species
    single_pokémon.nickname=nickname
    single_pokémon.dob=dob
    single_pokémon.trainer=trainer
    single_pokémon.treatment_notes=treatment_notes
    db.session.commit()
    return redirect (f"/pokémon/{id}")

@pokémon_blueprint.route("/pokémon/<id>/delete", methods = ["post"])
def delete_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    db.session.delete(single_pokémon)
    db.session.commit()
    return redirect("/pokémon")