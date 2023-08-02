from app import db
from flask_sqlalchemy import SQLAlchemy


class Pokédex(db.Model):
    __tablename__ = "Pokédex"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64), nullable=False)
    pokémon = db.relationship('Pokémon', backref='dex')

    def __repr__(self):
        return (f"Pokédex Entry #{self.id}, {self.name}")
    

import re

def id_from_string(string):
    id = ""
    for letter in string:
        match = re.match("[0-9]", letter)
        if match:
          id += letter
        if letter == ":":
            return int(id)