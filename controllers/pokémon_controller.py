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
    if nurse == "None":
        nurse = None
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

@pokémon_blueprint.route("/pokémon/<id>/edit")
def edit_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    nurses= Nurse.query.all()
    if single_pokémon.nurse != None:
        assigned_nurse = Nurse.query.get(single_pokémon.nurse)
    else:
        assigned_nurse = None
    return render_template("pokémon/edit_pokémon.jinja", single_pokémon=single_pokémon, nurses=nurses, assigned_nurse=assigned_nurse)

@pokémon_blueprint.route("/pokémon/<id>", methods=["post"])
def update_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    species=request.form['species']
    nickname=request.form['nickname']
    dob=request.form['date_of_birth']
    nurse=request.form['nurse']
    if nurse == "None":
        nurse = None
    treatment_notes=request.form['treatment_notes']
    contact=request.form['contact']
    nickname = empty_returns_null(nickname)
    dob = empty_returns_null(dob)
    treatment_notes = empty_returns_null(treatment_notes)
    single_pokémon.species=species
    single_pokémon.nickname=nickname
    single_pokémon.dob=dob
    single_pokémon.nurse=nurse
    single_pokémon.treatment_notes=treatment_notes
    single_pokémon.contact=contact
    db.session.commit()
    return redirect (f"/pokémon/{id}")

@pokémon_blueprint.route("/pokémon/<id>/delete", methods = ["post"])
def delete_pokémon(id):
    single_pokémon = Pokémon.query.get(id)
    db.session.delete(single_pokémon)
    db.session.commit()
    return redirect("/pokémon")