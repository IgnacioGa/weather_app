web: gunicorn --chdir config.wsgi -b 0.0.0.0:80 --timeout 350 --log-file -
release: python /app/manage.py migrate