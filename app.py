from flask import Flask, redirect, render_template, request, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'ein_sicherer_schlüssel'

# Festgelegte Anmeldeinformationen des Admins
ADMIN_USERNAME = 'William.Batling'
ADMIN_PASSWORD = 'VipVoyage'

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
            flash('Erfolgreich eingeloggt.')
            return redirect(url_for('booking_overview'))  # Geändert zu 'booking_overview'
        else:
            flash('Falscher Benutzername oder Passwort. Bitte versuchen Sie es erneut.')
    return render_template('login.html')

@app.route('/booking-overview')
def booking_overview():
    if not session.get('admin_logged_in'):
        flash('Bitte loggen Sie sich zuerst ein.')
        return redirect(url_for('login'))
    # Hier würden Sie Ihre Logik einfügen, um die Buchungsanfragen aus der Datenbank zu holen
    booking_requests = []  # Platzhalter für Datenbankabfrage
    return render_template('booking_overview.html', booking_requests=booking_requests)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash('Sie wurden erfolgreich ausgeloggt.')
    return redirect(url_for('home'))

@app.route('/inquiryoption')
def inquiry_option():
    # Sicherstellen, dass der Admin eingeloggt ist
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    return render_template('inquiryoption.html')

@app.route('/inquiryform-a')
def inquiryform_a():
    # Sicherstellen, dass der Admin eingeloggt ist
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    return render_template('inquiryform-a.html')

@app.route('/inquiryform-t')
def inquiryform_t():
    # Sicherstellen, dass der Admin eingeloggt ist
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    return render_template('inquiryform-t.html')


if __name__ == '__main__':
    app.run(debug=True)

