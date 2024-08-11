#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done
# python manage.py makemigrations
# until python manage.py migrate
# do
#     echo "Waiting for database to be ready..."
#     sleep 2
# done

python manage.py collectstatic --noinput    

# # Create superuser if it does not exist
# python manage.py shell << END
# from django.contrib.auth import get_user_model
# User = get_user_model()
# if not User.objects.filter(username='admin').exists():
#     User.objects.create_superuser('admin@admin.com', 'admin', 'admin')
# END

# for production server
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4

# for development server
# python manage.py runserver
