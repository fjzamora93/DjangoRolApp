web: gunicorn DjangoRolApp.wsgi --log-file -
worker: celery -A worker worker --loglevel=info