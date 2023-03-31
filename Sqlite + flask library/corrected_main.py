from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "lkjsldkjfksdf454854dfs"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app=app)

class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self):
        return f'{self.title}'

with app.app_context():
    db.create_all()
    book = books(3, 'model', 'abhinav', '10')
    db.session.add(book)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)