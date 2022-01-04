from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(40), default='message')
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    content = db.Column(db.Text, nullable=False)

    def __init__(self, name, content, email='', field='', phone=''):
        self.field = field
        self.name = name
        self.email = email
        self.phone = phone
        self.content = content

    def __str__(self):
        return f"Comment number {self.id}: sender_name:{self.name}"

db.create_all()