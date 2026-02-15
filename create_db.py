# create_db.py
from app import app, db

with app.app_context():
    db.create_all()
    print("Tables created (or already existed).")
    print("Database file should now be here →", app.config['SQLALCHEMY_DATABASE_URI'])