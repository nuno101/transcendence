set -e

cp -rf ../conf/avatars /data/media/
python manage.py runserver 0.0.0.0:8000