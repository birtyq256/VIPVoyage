import os
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from wtforms import Form, StringField, IntegerField, validators
from flask_migrate import Migrate





app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inquiries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Session(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

ADMIN_USERNAME = 'VipAgent'
ADMIN_PASSWORD = 'VipVoyage'


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
    status = db.Column(db.String(20), nullable=True)  


    def __init__(self, name, phone, arrival, departure, amount, budget, requests):
        self.name = name
        self.phone = phone
        self.arrival = arrival
        self.departure = departure
        self.amount = amount
        self.budget = budget
        self.requests = requests
        self.status = 'new'

def create_tables():
    with app.app_context():
        db.create_all()


class InquiryFormA(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    phone = StringField('Phone Number', [validators.Length(min=1, max=20)])
    arrival = StringField('Arrival', [validators.Length(min=1, max=100)])
    departure = StringField('Departure', [validators.Length(min=1, max=100)])
    amount = IntegerField('Amount of people', [validators.NumberRange(min=1)])
    budget = StringField('Budget', [validators.Length(min=1, max=100)])
    requests = StringField('Special Requests', [validators.Length(max=200)])
    status = StringField('Status', [validators.Length(max=20)])


class InquiryFormT(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    phone = StringField('Phone Number', [validators.Length(min=1, max=20)])
    arrival = StringField('Arrival', [validators.Length(min=1, max=100)])
    departure = StringField('Departure', [validators.Length(min=1, max=100)])
    arrival_time = StringField('Arrival Time', [validators.Length(min=1, max=100)])
    departure_time = StringField('Departure Time', [validators.Length(min=1, max=100)])
    amount = IntegerField('Amount of people', [validators.NumberRange(min=1)])
    budget = StringField('Budget', [validators.Length(min=1, max=100)])
    requests = StringField('Special Requests', [validators.Length(max=200)])
    status = StringField('Status', [validators.Length(max=20)])



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('overview')) 
        else:
            flash('Falscher Benutzername oder Passwort. Bitte versuchen Sie es erneut.')
    return render_template('login.html')

@app.route('/logout', methods=['GET'], endpoint='logout_get')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('home'))



@app.route('/overview')
def overview():
    inquiries = InquiryForm.query.all()
    return render_template('overview.html', inquiries=inquiries)






@app.route('/update_status/<int:inquiry_id>', methods=['POST'])
def update_status(inquiry_id):
    inquiry = InquiryForm.query.get_or_404(inquiry_id)
    status = request.form['status']
    inquiry.status = status
    db.session.commit()
    return redirect(url_for('overview'))

@app.route('/delete_inquiry/<int:inquiry_id>', methods=['POST'])
def delete_inquiry(inquiry_id):
    inquiry = InquiryForm.query.get_or_404(inquiry_id)
    db.session.delete(inquiry)
    db.session.commit()
    return redirect(url_for('overview'))




@app.route('/inquiryoption')
def inquiry_option():
    return render_template('inquiryoption.html')

@app.route('/inquiryform_a')
def inquiryform_a(): 
    return render_template('inquiryform_a.html')

@app.route('/inquiryform-t')
def inquiryform_t():
    return render_template('inquiryform_a.html')

@app.route('/submit_inquiry_a', methods=['POST'])
def submit_inquiry_a():
    form = InquiryFormA(request.form)
    if form.validate():
        new_inquiry = InquiryForm(
            name=form.name.data,
            phone=form.phone.data,
            arrival=form.arrival.data,
            departure=form.departure.data,
            amount=form.amount.data,
            budget=form.budget.data,
            requests=form.requests.data
        )
        db.session.add(new_inquiry)
        db.session.commit()
        return redirect(url_for('thank_you'))
    else:
        flash('Form validation failed. Please check the form and try again.', 'error')
        return redirect(url_for('inquiry_option_a'))

@app.route('/submit_inquiry_t', methods=['POST'])
def submit_inquiry_t():
    form = InquiryFormA(request.form)
    if form.validate():
        new_inquiry = InquiryForm(
            name=form.name.data,
            phone=form.phone.data,
            arrival=form.arrival.data,
            departure=form.departure.data,
            amount=form.amount.data,
            budget=form.budget.data,
            requests=form.requests.data
        )
        db.session.add(new_inquiry)
        db.session.commit()
        return redirect(url_for('thank_you'))
    else:
        flash('Form validation failed. Please check the form and try again.', 'error')
        return redirect(url_for('inquiry_option_a'))


@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
