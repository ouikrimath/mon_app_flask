import os

class Config:
    SECRET_KEY = 'ta_cle_secrete_a_changer'  # Change-la par une vraie clé secrète pour la prod
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Dossier où seront stockés les fichiers uploadés
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'docs')

    # Taille maximale upload (ici 16 Mo)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
