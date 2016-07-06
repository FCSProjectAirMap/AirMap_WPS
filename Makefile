migrate:
	- python airmap/manage.py makemigrations airmap users
	- python airmap/manage.py migrate
