from app import db
from flask_sqlalchemy import SQLAlchemy


class Pokédex(db.Model):
    __tablename__ = "Pokédex"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return (f"Pokédex Entry #{self.id}, {self.name}")