from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class InquiryForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    arrival = db.Column(db.String(100), nullable=True)
    departure = db.Column(db.String(100), nullable=True)
    arrival_time = db.Column(db.String(100), nullable=True)
    departure_time = db.Column(db.String(100), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.String(100), nullable=False)
    requests = db.Column(db.String(200), nullable=True)

def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.create_all()
