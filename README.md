# cgl-django
Projet Culture Gnu/Linux - Django

## Environnement
`virtualenv -p python3 venv`

si conda activé --> `conda deactivate`

`source venv/bin/activate`

## Dépendances
`sudo apt-get install python-virtualenv python-pip libmysqlclient-dev python3-dev mysql-server`

`pip install django==2.2.17`

`pip install mysqlclient`

## BDD
`sudo systemctl start mysql`

`sudo mysql -uroot`

`CREATE USER djangoadmin@localhost IDENTIFIED by 'django';`

`CREATE DATABASE decouverte CHARACTER SET utf8;`

`GRANT ALL on decouverte.* to djangoadmin@localhost;`

`flush privileges;`

`quit;`

## Initialiser la BDD
`cd mopga`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py createsuperuser`


## Lancer le serveur
`cd mopga`

`python manage.py runserver`

http://127.0.0.1:8000
