"""
Configuration file for the Online Voting System
"""

import os
from datetime import timedelta

# Base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flask Configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')
DEBUG = os.environ.get('FLASK_DEBUG', True)
TESTING = False

# Database Configuration
INSTANCE_PATH = os.path.join(BASE_DIR, 'instance')
os.makedirs(INSTANCE_PATH, exist_ok=True)
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(INSTANCE_PATH, "votes.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Session Configuration
PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Application Settings
APP_NAME = 'Online Voting System'
APP_VERSION = '1.0.0'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Voting Settings
ALLOW_MULTIPLE_VOTES = False  # Set to True to allow users to change their vote
VOTING_ENABLED = True

# Security Settings
PASSWORD_MIN_LENGTH = 6
USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 80

# Email Configuration (for future use)
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# Logging Configuration
LOG_LEVEL = 'INFO'
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configuration for MariaDB Database
DB_CONFIG = {
    'DB_ENGINE': 'mysql+pymysql',
    'SQLALCHEMY_DATABASE_URI': 'mysql+pymysql://{Username}@{Host}:{Port}/{DatabaseName}',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'DatabaseName': 'online_voting_system',
    'Username': 'root',
    'Password': '',  # Empty password since we're not using one
    'Host': 'localhost',
    'Port': '3306'
}