migrate:
	- python airmap/manage.py makemigrations airmap users roots
	- python airmap/manage.py migrate
