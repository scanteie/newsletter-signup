from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv
import io
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

# Use PostgreSQL in production, SQLite in development
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    # Heroku/Render style PostgreSQL URL
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='subscribed')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# Authentication decorator
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != os.environ.get('ADMIN_USER', 'admin') or \
           auth.password != os.environ.get('ADMIN_PASS', 'admin'):
            return ('Could not verify your access level for that URL.\n'
                   'You have to login with proper credentials', 401,
                   {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    return redirect(url_for('subscribe'))

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        agreed_to_terms = request.form.get('terms') == 'on'

        if not email or not agreed_to_terms:
            flash('Please provide an email and accept the terms.', 'error')
            return render_template('subscribe.html')

        try:
            subscriber = Subscriber(email=email)
            db.session.add(subscriber)
            db.session.commit()
            return redirect(url_for('thank_you'))
        except:
            db.session.rollback()
            flash('This email is already subscribed.', 'error')
            return render_template('subscribe.html')

    return render_template('subscribe.html')

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        email = request.form.get('email')
        subscriber = Subscriber.query.filter_by(email=email).first()

        if subscriber:
            subscriber.status = 'unsubscribed'
            db.session.commit()
            flash('Successfully unsubscribed.', 'success')
        else:
            flash('Email not found.', 'error')

    return render_template('unsubscribe.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/view-terms')
def view_terms():
    return redirect(url_for('terms'))

@app.route('/admin')
@requires_auth
def admin():
    subscribers = Subscriber.query.all()
    return render_template('admin.html', subscribers=subscribers)

@app.route('/admin/export')
@requires_auth
def export():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Email', 'Status', 'Created At', 'Updated At'])

    subscribers = Subscriber.query.all()
    for subscriber in subscribers:
        writer.writerow([
            subscriber.email,
            subscriber.status,
            subscriber.created_at,
            subscriber.updated_at
        ])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'subscribers_{datetime.now().strftime("%Y%m%d")}.csv'
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)