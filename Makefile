install:
	pip install -r requirements.txt

run:
	python3 manage.py runserver 0.0.0.0:7676

shell:
	python3 manage.py shell

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate


pipe:
	make install
	make migrate
	make run
