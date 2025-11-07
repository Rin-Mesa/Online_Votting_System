# Roles and Permissions

This document describes the role-based access control system in the Online Voting System.

## User Roles

### 1. Normal User
A regular user who can view candidates and cast votes.

**Permissions:**
- ✓ Register account
- ✓ Login
- ✓ View candidates
- ✓ Cast vote (one vote per user)
- ✓ View voting results
- ✓ Logout

**Restrictions:**
- ✗ Cannot access admin panel
- ✗ Cannot add/delete candidates
- ✗ Cannot manage users
- ✗ Cannot reset votes
- ✗ Cannot vote multiple times

**Access Routes:**
- `/register` - Register new account
- `/login` - Login
- `/vote` - Cast vote
- `/results` - View results
- `/logout` - Logout

---

### 2. Admin User
An administrator with full system access and control.

**Permissions:**
- ✓ All normal user permissions
- ✓ Access admin panel
- ✓ Add new candidates
- ✓ Delete candidates
- ✓ View all registered users
- ✓ Delete user accounts
- ✓ Reset all votes
- ✓ View voting statistics

**Restrictions:**
- ✗ Cannot vote (admin cannot participate in voting)
- ✗ Cannot delete their own account

**Access Routes:**
- `/admin` - Admin panel
- All normal user routes (except `/vote`)

---

## Access Control Rules

### Route Protection

| Route | Normal User | Admin | Not Logged In |
|-------|------------|-------|--------------|
| `/` | ✓ | ✓ | ✓ |
| `/register` | ✓ | ✓ | ✓ |
| `/login` | ✓ | ✓ | ✓ |
| `/vote` | ✓ | ✗ (redirects to admin) | ✗ (redirects to login) |
| `/results` | ✓ | ✓ | ✗ (redirects to login) |
| `/admin` | ✗ (redirects to login) | ✓ | ✗ (redirects to login) |
| `/logout` | ✓ | ✓ | ✓ |

### Voting Rules

1. **One Vote Per User**: Each user can only vote once
2. **Admin Cannot Vote**: Admins are redirected to admin panel when accessing `/vote`
3. **Vote Verification**: System checks if user has already voted before allowing new vote
4. **Vote Counting**: Votes are automatically counted and displayed in real-time

### User Management

1. **User Deletion**: Admins can delete any user except themselves
2. **Vote Cleanup**: When a user is deleted, their vote is also removed
3. **Admin Protection**: Current admin cannot be deleted by themselves

---

## Default Admin Account

**Username:** `admin`
**Password:** `admin123`

⚠️ **IMPORTANT:** Change these credentials immediately in production!

---

## Creating Additional Admin Accounts

To create another admin account, use the Python shell:

```python
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User(
        username='admin2',
        password=generate_password_hash('secure_password'),
        is_admin=True
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user created!")
```

---

## Admin Panel Features

### Candidate Management
- **Add Candidate**: Add new candidates with name and description
- **Delete Candidate**: Remove candidates from the system
- **View Candidates**: See all candidates and their vote counts

### User Management
- **View Users**: See all registered users with their roles
- **Delete Users**: Remove user accounts (except current admin)
- **User Roles**: Identify which users are admins and which are normal users

### Voting Management
- **View Statistics**: See total votes cast
- **Reset Votes**: Clear all votes and start fresh
- **Vote Tracking**: Monitor voting progress in real-time

---

## Security Considerations

1. **Session Management**: Users are logged in via sessions
2. **Password Hashing**: All passwords are hashed using Werkzeug
3. **Admin-Only Routes**: Admin routes check for `is_admin` flag
4. **Vote Integrity**: One vote per user is enforced at database level
5. **User Deletion**: Cascading delete removes associated votes

---

## Workflow Examples

### Normal User Workflow
1. User registers account
2. User logs in
3. User views candidates
4. User casts vote
5. User views results
6. User logs out

### Admin Workflow
1. Admin logs in
2. Admin accesses admin panel
3. Admin manages candidates (add/delete)
4. Admin manages users (view/delete)
5. Admin monitors voting progress
6. Admin can reset votes if needed
7. Admin logs out

---

## Troubleshooting

### User Cannot Vote
- Check if user is logged in
- Check if user is an admin (admins cannot vote)
- Check if user has already voted

### Cannot Access Admin Panel
- Verify user is logged in
- Verify user has admin privileges (`is_admin=True`)
- Check session is not expired

### Cannot Delete User
- Verify you are logged in as admin
- Verify you are not trying to delete yourself
- Check user exists in database

---

## Future Enhancements

- [ ] Role-based permissions system
- [ ] Multiple admin levels
- [ ] Audit logging for admin actions
- [ ] User activity tracking
- [ ] Permission management interface
- [ ] Two-factor authentication for admins

---

## Support

For issues or questions about roles and permissions, refer to:
- README.md - Full documentation
- QUICKSTART.md - Quick start guide
- app.py - Source code with detailed comments

