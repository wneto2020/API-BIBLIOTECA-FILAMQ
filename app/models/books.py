from datetime import datetime
from app import db, ma


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(16), unique=True, nullable=False)
    company = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200))
    authors = db.Column(db.String(200), nullable=False)
    inserted_on = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title, company, image, authors):
        self.title = title
        self.company = company
        self.image = image
        self.authors = authors


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'company', 'image', 'authors', 'inserted_on')


book_schema = BookSchema()
books_schema = BookSchema(many=True)
