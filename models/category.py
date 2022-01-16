from config import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    name = db.Column(db.String(30), nullable=False, unique=True)
    is_sub = db.Column(db.Boolean, nullable=False)

    def __init__(self, parent_id, name, is_sub):
        self.parent_id = parent_id
        self.name = name
        self.is_sub = is_sub

    def __repr__(self):
        return f"Category | {self.id} : {self.name}"

