migrate:
	- python airmap/manage.py makemigrations airmap users travels
	- python airmap/manage.py migrate
