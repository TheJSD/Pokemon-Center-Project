from flask import Flask, Blueprint, render_template, request, redirect
from models.nurse_model import Nurse
from models.trainer_model import Trainer
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
    assigned_trainers = Trainer.query.filter_by(nurse = id).all()
    return render_template("nurses/show_nurse.jinja", nurse=nurse, assigned_trainers=assigned_trainers)

@nurses_blueprint.route("/nurses/<id>/edit")
def edit_nurse(id):
    nurse = Nurse.query.get(id)
    return render_template ("nurses/edit_nurse.jinja", nurse=nurse)

@nurses_blueprint.route("/nurses/<id>", methods=["post"])
def update_nurse(id):
    nurse= Nurse.query.get(id)
    name = request.form["name"]
    nurse.name = name
    db.session.commit()
    return redirect (f"/nurses/{id}")

@nurses_blueprint.route("/nurses/<id>/delete", methods = ["post"])
def delete_nurse(id):
    nurse = Nurse.query.get(id)
    assigned_trainers= Trainer.query.filter_by(nurse = id)
    for trainer in assigned_trainers:
        trainer.nurse = None
    db.session.delete(nurse)
    db.session.commit()
    return redirect("/nurses")