"""Database models."""
from datetime import datetime, timezone
from service import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(40))
    date_joined = db.Column(db.DateTime, nullable=False,
                            default=lambda: datetime.now(timezone.utc))

    def serialize(self):
        return {
            "id": self.id, "name": self.name, "email": self.email,
            "address": self.address, "phone_number": self.phone_number,
            "date_joined": self.date_joined.isoformat(),
        }

    def update_from(self, data):
        for field in ("name", "email", "address", "phone_number"):
            if field in data:
                setattr(self, field, data[field])
