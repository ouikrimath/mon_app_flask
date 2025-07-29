# base_de_donnees.py

from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(
        username="admin",
        password=generate_password_hash("admin123"),
        role="admin"
    )

    user = User(
        username="utilisateur",
        password=generate_password_hash("user123"),
        role="utilisateur"
    )

    db.session.add(admin)
    db.session.add(user)
    db.session.commit()

    print("✅ Base de données initialisée avec utilisateurs.")
