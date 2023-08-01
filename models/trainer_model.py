from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

class Trainer(db.Model):
    __tablename__ = "Trainers"

    id=db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name=db.Column(db.String(64), nullable=False)
    contact=db.Column(db.Text, nullable=False)
    nurse = db.Column(UUID(as_uuid=True), db.ForeignKey('Nurses.id'))
    pokémon = db.relationship('Pokémon', backref='owner')

    def __repr__(self):
        return (f"<Trainer: {self.name}, {self.id}>")