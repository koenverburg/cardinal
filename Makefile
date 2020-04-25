freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

check:
	flake8 cardinal.py
