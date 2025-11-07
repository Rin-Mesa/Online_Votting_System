"""
Setup script for the Online Voting System
Run this script to initialize the database and create an admin user
"""

import os
import sys
from app import app, db, User, Candidate
from werkzeug.security import generate_password_hash


def create_admin_user(username='admin', password='admin123'):
    """Create an admin user"""
    with app.app_context():
        # Check if admin already exists
        existing_admin = User.query.filter_by(username=username).first()
        if existing_admin:
            print(f"Admin user '{username}' already exists!")
            return False
        
        admin = User(
            username=username,
            password=generate_password_hash(password),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print(f"✓ Admin user '{username}' created successfully!")
        print(f"  Username: {username}")
        print(f"  Password: {password}")
        return True


def create_sample_candidates():
    """Create sample candidates"""
    with app.app_context():
        # Check if candidates already exist
        if Candidate.query.first():
            print("Candidates already exist in the database!")
            return False
        
        candidates = [
            Candidate(
                name='Alice Johnson',
                description='Experienced leader with 10 years in public service'
            ),
            Candidate(
                name='Bob Smith',
                description='Tech entrepreneur focused on innovation'
            ),
            Candidate(
                name='Carol Williams',
                description='Environmental advocate and community organizer'
            ),
            Candidate(
                name='David Brown',
                description='Healthcare professional with medical background'
            ),
        ]
        
        for candidate in candidates:
            db.session.add(candidate)
        
        db.session.commit()
        print(f"✓ {len(candidates)} sample candidates created successfully!")
        for candidate in candidates:
            print(f"  - {candidate.name}")
        return True


def initialize_database():
    """Initialize the database"""
    with app.app_context():
        print("Initializing database...")
        db.create_all()
        print("✓ Database initialized successfully!")


def main():
    """Main setup function"""
    print("=" * 50)
    print("Online Voting System - Setup")
    print("=" * 50)
    print()
    
    # Initialize database
    initialize_database()
    print()
    
    # Create admin user
    print("Creating admin user...")
    admin_created = create_admin_user()
    print()
    
    # Create sample candidates
    print("Creating sample candidates...")
    candidates_created = create_sample_candidates()
    print()
    
    print("=" * 50)
    print("Setup Complete!")
    print("=" * 50)
    print()
    print("Next steps:")
    print("1. Run: python app.py")
    print("2. Open: http://localhost:5000")
    print("3. Login with admin credentials")
    print()
    print("For more information, see README.md or QUICKSTART.md")
    print()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error during setup: {e}")
        sys.exit(1)

