# Online Voting System

A secure, transparent, and easy-to-use web-based voting platform built with Flask and SQLAlchemy.

## Features

- **User Authentication**: Secure registration and login system
- **Voting**: Users can cast their vote for candidates
- **Results**: Real-time voting results with visual progress bars
- **Admin Panel**: Manage candidates, view registered users, and reset votes
- **Responsive Design**: Works on desktop and mobile devices
- **Database**: SQLite database for persistent data storage

## Project Structure

```
online_voting_system/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
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
└── instance/             # Instance folder (auto-created)
    └── votes.db          # SQLite database (auto-created)
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd online_voting_system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`

## Usage

### For Regular Users

1. **Register**: Create a new account with a username and password
2. **Login**: Log in with your credentials
3. **Vote**: Select a candidate and submit your vote
4. **View Results**: See the voting results with percentages and vote counts

### For Administrators

1. **Login**: Use an admin account (must be set up in the database)
2. **Admin Panel**: Access the admin panel to:
   - Add new candidates
   - Delete candidates
   - View registered users
   - Reset all votes

## Database Models

### User
- `id`: Primary key
- `username`: Unique username
- `password`: Hashed password
- `is_admin`: Boolean flag for admin privileges
- `created_at`: Account creation timestamp

### Candidate
- `id`: Primary key
- `name`: Candidate name
- `description`: Candidate description
- `votes`: Vote count
- `created_at`: Creation timestamp

### Vote
- `id`: Primary key
- `user_id`: Foreign key to User
- `candidate_id`: Foreign key to Candidate
- `created_at`: Vote timestamp

## Security Features

- Password hashing using Werkzeug
- Session-based authentication
- One vote per user enforcement
- Admin-only access to admin panel
- CSRF protection ready (can be enhanced with Flask-WTF)

## Configuration

Edit `app.py` to modify:
- `SECRET_KEY`: Change this to a secure random string in production
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- Debug mode: Set `debug=False` in production

## Future Enhancements

- Email verification for registration
- Two-factor authentication
- Vote encryption
- Audit logging
- Export results to CSV/PDF
- Multiple voting rounds
- Real-time result updates with WebSockets

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.

