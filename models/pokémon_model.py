from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

class Pokémon(db.Model):
    __tablename__ = "Pokémon"

    id=db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    species = db.Column(db.String(64), nullable=False)
    nickname = db.Column(db.String(64))
    contact = db.Column(db.String(64), nullable=False)
    dob = db.Column(UUID(as_uuid=True), db.ForeignKey('Trainers.id'))
    treatment_notes = db.Column(db.Text())
    nurse = db.Column(UUID(as_uuid=True), db.ForeignKey('Nurses.id'))

    def __repr__(self):
        return (f"<Nurse: {self.name}, {self.id}>")
    


def empty_returns_null(field):
    if field != "":
        return field