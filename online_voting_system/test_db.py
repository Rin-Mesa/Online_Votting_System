from app import app, db

print("[INFO] Testing database connection...")

try:
    with app.app_context():
        # This will create all tables if they don't exist
        db.create_all()
        print("[SUCCESS] Database connection successful!")
        print("[SUCCESS] Tables created/verified successfully!")
        
        # List all tables
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        print("\n[INFO] Database tables:")
        for table_name in inspector.get_table_names():
            print(f"- {table_name}")
            
except Exception as e:
    print(f"[ERROR] Database connection failed: {str(e)}")
    print("\nTroubleshooting steps:")
    print("1. Make sure MySQL server is running")
    print("2. Check your MySQL credentials in config.py")
    print("3. Verify the database 'online_voting_system' exists")
    print("4. Ensure the MySQL user has proper permissions")
