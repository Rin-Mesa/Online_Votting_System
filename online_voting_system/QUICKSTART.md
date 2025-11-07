# Quick Start Guide

## Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

---

## First Time Setup

### Create an Admin Account

To create an admin account, you need to modify the database directly or use Python shell:

```bash
python
```

Then in the Python shell:
```python
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Create admin user
    admin = User(
        username='admin',
        password=generate_password_hash('admin123'),
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user created!")
```

### Add Sample Candidates

After logging in as admin, go to the Admin Panel and add candidates:
- Click "Add Candidate"
- Enter candidate name and description
- Click "Add Candidate"

---

## Testing the System

### As a Regular User:
1. Register a new account
2. Login with your credentials
3. Cast your vote
4. View results

### As an Admin:
1. Login with admin credentials
2. Access Admin Panel
3. Manage candidates
4. View registered users
5. Reset votes if needed

---

## Project Structure

```
online_voting_system/
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies
├── README.md             # Full documentation
├── QUICKSTART.md         # This file
├── .gitignore            # Git ignore rules
│
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── vote.html         # Voting page
│   ├── results.html      # Results page
│   └── admin.html        # Admin panel
│
├── static/               # Static files
│   ├── css/
│   │   └── styles.css    # Stylesheet
│   └── js/
│       └── main.js       # JavaScript
│
└── instance/             # Instance folder
    └── votes.db          # SQLite database
```

---

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change port here
```

### Database Issues
To reset the database:
1. Delete `instance/votes.db`
2. Run `python app.py` again
3. The database will be recreated automatically

### Module Not Found
Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

---

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize the styling in `static/css/styles.css`
- Add more features as needed
- Deploy to production (see README.md for security recommendations)

---

## Support

For issues or questions, refer to the README.md file or check the Flask documentation at https://flask.palletsprojects.com/

