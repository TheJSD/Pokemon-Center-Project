from flask import Flask, Blueprint, render_template, request, redirect
from models.pokémon_model import Pokémon, empty_returns_null
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
    nurse = Nurse.query.get(single_pokémon.nurse)
    return render_template("pokémon/show_pokémon.jinja", single_pokémon=single_pokémon, nurse=nurse)

@pokémon_blueprint.route("/pokémon/new_pokémon")
def register_pokémon_page():
    nurses = Nurse.query.all()
    return render_template("pokémon/new_pokémon.jinja", nurses=nurses)

@pokémon_blueprint.route("/pokémon", methods=["post"])
def add_pokemon():
    species=request.form['species']
    nickname=request.form['nickname']
    dob=request.form['date_of_birth']
    nurse=request.form['nurse']
    treatment_notes=request.form['treatment_notes']
    contact=request.form['contact']
    nickname = empty_returns_null(nickname)
    dob = empty_returns_null(dob)
    treatment_notes = empty_returns_null(treatment_notes)
    new_pokémon = Pokémon(species=species,
                    nickname=nickname,
                    dob=dob,
                    nurse=nurse,
                    contact=contact,
                    treatment_notes=treatment_notes)
    db.session.add(new_pokémon)
    db.session.commit()
    return redirect ("/pokémon")