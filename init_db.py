#use when db changes and need to start fresh
from flask import Flask
from app import app, db
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database initialized!")

if __name__ == "__main__":
    init_db()
