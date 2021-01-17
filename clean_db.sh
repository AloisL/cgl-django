#!/bin/bash

HOME_DIR=$(pwd)

echo "Removing sb.sqlite3..."
rm db.sqlite3

cd mopga/modules/
for d in */ ; do
    echo "Removing db init files in module $d"
    rm $d/migrations/0* 2> /dev/null
done

cd $HOME_DIR

echo "Starting db makemigrations..."
python manage.py makemigrations

echo "Starting db migrate..."
python manage.py migrate