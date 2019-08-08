web: gunicorn iot_dashboard.wsgi
release: python manage.py makemigrations --merge
release: python manage.py migrate