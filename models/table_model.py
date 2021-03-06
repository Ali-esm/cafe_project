from app import db


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False, unique=True)
    position = db.Column(db.String(2), nullable=False, unique=True)
