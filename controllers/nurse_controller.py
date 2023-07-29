from flask import Flask, Blueprint, render_template, request, redirect
from models.pokémon_model import Pokémon
from models.nurse_model import Nurse
from app import db

nurses_blueprint=Blueprint("nurses", __name__)

@nurses_blueprint.route("/nurses")
def nurses():
    nurses = Nurse.query.all()
    return render_template("nurses/index.jinja", nurses=nurses)


@nurses_blueprint.route("/nurses/new")
def register_nurse():
    return render_template("nurses/new_nurse.jinja")

@nurses_blueprint.route("/nurses", methods=["post"])
def add_nurse():
    name = request.form["name"]
    new_nurse = Nurse(name=name)
    db.session.add(new_nurse)
    db.session.commit()
    return redirect("/nurses")

@nurses_blueprint.route("/nurses/<id>")
def show_nurse(id):
    nurse = Nurse.query.get(id)
    return render_template("nurses/show_nurse.jinja", nurse=nurse)