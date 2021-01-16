# cgl-django
Projet Culture Gnu/Linux - Django

## Environnement
`virtualenv -p python3 venv`

si conda activé --> `conda deactivate`

`source venv/bin/activate`

## Dépendances
`sudo apt-get install python-virtualenv python-pip python3-dev`

`pip install django==2.2.17`


## Initialiser la BDD
`cd mopga`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`


## Lancer le serveur
`cd mopga`

`python manage.py runserver`

http://127.0.0.1:8000

Pour lancer l'application, télécharger les sources. Dans le dossier de l'application, entrer: docker-compose up (-d pour détacher).
