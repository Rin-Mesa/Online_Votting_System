from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# Create instance folder if it doesn't exist
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
os.makedirs(instance_path, exist_ok=True)

db_path = os.path.join(instance_path, 'votes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')
        
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            
            if user.is_admin:
                return redirect(url_for('admin'))
            return redirect(url_for('vote'))
        
        return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Prevent admin from voting
    if session.get('is_admin'):
        return redirect(url_for('admin'))

    if request.method == 'POST':
        candidate_id = request.form.get('candidate_id')

        # Check if user already voted
        existing_vote = Vote.query.filter_by(user_id=session['user_id']).first()
        if existing_vote:
            # Allow changing vote: decrement old candidate's votes
            old_candidate = Candidate.query.get(existing_vote.candidate_id)
            if old_candidate:
                old_candidate.votes -= 1
            # Update the vote record to new candidate
            existing_vote.candidate_id = candidate_id
            existing_vote.created_at = datetime.utcnow()
        else:
            # First time voting
            vote = Vote(user_id=session['user_id'], candidate_id=candidate_id)
            db.session.add(vote)

        # Increment new candidate's votes
        candidate = Candidate.query.get(candidate_id)
        candidate.votes += 1

        db.session.commit()

        return redirect(url_for('results'))

    candidates = Candidate.query.all()
    return render_template('vote.html', candidates=candidates)

@app.route('/results')
def results():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    candidates = Candidate.query.order_by(Candidate.votes.desc()).all()
    total_votes = sum(c.votes for c in candidates)
    return render_template('results.html', candidates=candidates, total_votes=total_votes)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'user_id' not in session or not session.get('is_admin'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add_candidate':
            name = request.form.get('name')
            description = request.form.get('description')
            candidate = Candidate(name=name, description=description)
            db.session.add(candidate)
            db.session.commit()

        elif action == 'delete_candidate':
            candidate_id = request.form.get('candidate_id')
            Candidate.query.filter_by(id=candidate_id).delete()
            db.session.commit()

        elif action == 'reset_votes':
            Candidate.query.update({'votes': 0})
            Vote.query.delete()
            db.session.commit()

        elif action == 'edit_candidate':
            candidate_id = request.form.get('candidate_id')
            name = request.form.get('name')
            description = request.form.get('description')
            candidate = Candidate.query.get(candidate_id)
            if candidate:
                candidate.name = name
                candidate.description = description
                # Do not update votes from form - votes are managed by the voting system
                db.session.commit()

        elif action == 'delete_user':
            user_id = request.form.get('user_id')
            # Prevent deleting the current admin
            if int(user_id) != session['user_id']:
                Vote.query.filter_by(user_id=user_id).delete()
                User.query.filter_by(id=user_id).delete()
                db.session.commit()

    candidates = Candidate.query.all()
    users = User.query.all()
    total_votes = sum(c.votes for c in candidates)
    return render_template('admin.html', candidates=candidates, users=users, total_votes=total_votes)

@app.route('/api/candidates')
def api_candidates():
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'votes': c.votes} for c in candidates])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

