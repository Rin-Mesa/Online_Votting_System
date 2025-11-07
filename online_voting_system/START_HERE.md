# 🗳️ Online Voting System - START HERE

Welcome! Your online voting system has been successfully initialized and is ready to use.

## ⚡ Quick Start (2 Commands)

```bash
# Step 1: Run the setup script (creates admin user and sample candidates)
python setup.py

# Step 2: Start the application
python app.py
```

Then open your browser to: **http://localhost:5000**

## 📚 Documentation Guide

Choose what you need:

| Document | Purpose |
|----------|---------|
| **START_HERE.md** | This file - Quick overview |
| **QUICKSTART.md** | Fast setup and testing guide |
| **README.md** | Complete documentation |
| **SETUP_COMPLETE.md** | What was created |
| **VERIFICATION.md** | Verification checklist |

## 🎯 What You Can Do

### As a Regular User
1. Register a new account
2. Login with your credentials
3. Cast your vote for a candidate
4. View live voting results

### As an Administrator
1. Login with admin credentials (admin / admin123)
2. Add new candidates
3. Delete candidates
4. View all registered users
5. Reset all votes

## 📁 Project Structure

```
online_voting_system/
├── app.py              ← Main application
├── setup.py            ← Run this first!
├── config.py           ← Configuration
├── requirements.txt    ← Dependencies
├── templates/          ← HTML pages (6 files)
├── static/             ← CSS & JavaScript
└── instance/           ← Database (auto-created)
```

## 🔑 Default Credentials

**Admin Account:**
- Username: `admin`
- Password: `admin123`

⚠️ Change these in production!

## 🚀 Getting Started

### First Time Setup

```bash
# 1. Install dependencies (if not already done)
pip install -r requirements.txt

# 2. Run setup script
python setup.py

# 3. Start the server
python app.py

# 4. Open browser
# http://localhost:5000
```

### Testing the System

1. **Register a new user:**
   - Click "Register"
   - Enter username and password
   - Click "Register"

2. **Login:**
   - Click "Login"
   - Enter your credentials
   - Click "Login"

3. **Cast a vote:**
   - Select a candidate
   - Click "Submit Vote"

4. **View results:**
   - Click "Results"
   - See live voting statistics

5. **Admin panel:**
   - Login as admin (admin/admin123)
   - Click "Admin Panel"
   - Manage candidates and users

## 🎨 Features

✅ User registration and authentication
✅ Secure voting (one vote per user)
✅ Real-time results with charts
✅ Admin panel for management
✅ Responsive design (mobile-friendly)
✅ SQLite database
✅ Session management
✅ Password hashing

## 🔧 Customization

### Change Admin Password
Edit `setup.py` and modify the `create_admin_user()` call.

### Change Port
Edit `app.py` and change the port in the last line:
```python
app.run(debug=True, port=5001)  # Change 5000 to 5001
```

### Customize Styling
Edit `static/css/styles.css` to change colors and layout.

## 🐛 Troubleshooting

### Port 5000 Already in Use
Change the port in `app.py` (see Customization above).

### Database Error
Delete `instance/votes.db` and run `python setup.py` again.

### Module Not Found
Run: `pip install -r requirements.txt`

## 📞 Need Help?

- **Quick questions?** → See QUICKSTART.md
- **Full documentation?** → See README.md
- **What was created?** → See SETUP_COMPLETE.md
- **Verify setup?** → See VERIFICATION.md

## ✨ Next Steps

1. Run `python setup.py` to initialize
2. Run `python app.py` to start
3. Open http://localhost:5000
4. Test the system
5. Customize as needed

## 🎉 You're Ready!

Everything is set up and ready to go. Just run:

```bash
python setup.py
python app.py
```

Then visit http://localhost:5000

---

**Happy Voting! 🗳️**

For more details, see the other documentation files in this directory.

