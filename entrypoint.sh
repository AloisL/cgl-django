\cp -r /mopga/dump/data/ /mopga/mopga/static/
\cp -r /mopga/dump/db.sqlite3 /mopga

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000