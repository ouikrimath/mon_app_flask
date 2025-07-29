from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'  # Change-la pour la production !

UPLOAD_FOLDER = 'uploads'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Exemple simple, à remplacer par ta gestion réelle
        if username == 'admin' and password == 'admin123':
            session['username'] = username
            session['role'] = 'admin'
            return redirect(url_for('dashboard'))
        elif username == 'user' and password == 'user123':
            session['username'] = username
            session['role'] = 'utilisateur'
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', erreur="Nom d'utilisateur ou mot de passe incorrect.")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'], role=session['role'])

@app.route('/documents/<categorie>')
def documents(categorie):
    if 'username' not in session:
        return redirect(url_for('login'))

    chemin = os.path.join(UPLOAD_FOLDER, categorie)
    fichiers = []
    dates = {}

    if os.path.exists(chemin):
        fichiers = os.listdir(chemin)
        for f in fichiers:
            chemin_complet = os.path.join(chemin, f)
            try:
                date_modif = datetime.fromtimestamp(os.path.getmtime(chemin_complet))
                dates[f] = date_modif.strftime("%d/%m/%Y %H:%M")
            except Exception:
                dates[f] = "Inconnue"

    return render_template(
        'documents.html',
        fichiers=fichiers,
        dates=dates,  # Bien passer cette variable
        categorie=categorie,
        username=session.get('username'),
        role=session.get('role')
    )

@app.route('/uploads/<categorie>/<nom_fichier>')
def telecharger_fichier(categorie, nom_fichier):
    chemin = os.path.join(UPLOAD_FOLDER, categorie)
    return send_from_directory(chemin, nom_fichier)

if __name__ == '__main__':
    app.run(debug=True)
