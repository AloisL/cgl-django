# cgl-django
Projet Culture Gnu/Linux - Django

## Environnement
`virtualenv -p python3 venv`
si conda activé --> `conda deactivate`
`source venv/bin/activate`

## Dépendances
`sudo apt-get install python-virtualenv python-pip python3-dev`
`pip install django==2.2.17`
`requirement.txt`

## Initialiser la BDD
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py createsuperuser`

## Lancer le serveur
`python manage.py runserver`
http://127.0.0.1:8000

## Lancement en mode "production" avec chargement d'un dump:
### Méthode 1
Script "start.sh"

### Méthode 2
1) Se placer à la racine
2) docker build . -t mopga
3) docker run -t -p 8000:8000 mopga:latest