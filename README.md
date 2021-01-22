# cgl-django
Projet Culture Gnu/Linux - Django

## Lancement en mode "production" avec chargement d'un dump:
### Méthode 1 (par défaut)
1) Se placer à la racine du projet
2) `chmod +x start.sh`
3) `./start.sh`
4) Serveur disponible @ http://127.0.0.1:8000

### Méthode 2
1) Se placer à la racine du projet
2) `docker build . -t mopga`
3) `docker run -t -p 8000:8000 mopga:latest`
4) Serveur disponible @ http://127.0.0.1:8000

### Utilisateurs disponibles via le dumb

#### Porteurs de projet :
- maker1
- maker2
- maker3
#### Financeur de projet :
- funder1

#### Evaluateur de projet :
- rater1

#### Superutilisateur (interface administration)
- superuser

#### Mot de passe commun à tous les utilisateurs
- S4UdRt2CbxDteRk

## Lancement local en mode "dev" sans chargement d'un dump
### Environnement
`virtualenv -p python3 venv`

(`conda deactivate`)

`source venv/bin/activate`

### Dépendances
`sudo apt-get install python-virtualenv python-pip python3-dev`

`pip install -r requirements.txt`

### Initialiser la BDD
`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`

### Lancer le serveur
`python manage.py runserver`

Serveur disponible @ http://127.0.0.1:8000