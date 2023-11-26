freeze:
	python3 -m pip freeze > requirements.txt

install:
	python3 -m pip install -r requirements.txt

make-venv:
	python3.11 -m venv venv
