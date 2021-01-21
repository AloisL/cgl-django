mv /mopga/dump/data/ /mopga/static/
mv /mopga/dump/db.sqlite3 /mopga

rm -rf /mopga/dump

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000