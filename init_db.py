print("Début init_db.py")

from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    print("Création des tables...")
    db.create_all()
    print("Tables créées")

    admin = User(username='admin', password=generate_password_hash('admin123'), role='admin')
    db.session.add(admin)
    db.session.commit()

    print("Utilisateur admin ajouté.")
