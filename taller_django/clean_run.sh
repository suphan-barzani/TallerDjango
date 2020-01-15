find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
echo Removing database...
rm db.sqlite3

python manage.py makemigrations
python manage.py migrate

sh run.sh
