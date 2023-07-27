from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

# I used sql command "CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; in sql to add uuid functions for id"
class Nurse(db.Model):
    __tablename__ = "Nurses"

    id=db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name=db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return (f"<Nurse: {self.name}, {self.id}>")