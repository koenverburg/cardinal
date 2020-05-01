freeze:
	pipreqs . --force

install:
	pip install -r requirements.txt

check:
	flake8 cardinal.py
