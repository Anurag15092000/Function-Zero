install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest  test_scrape.py

format:
	black *.py
lint:
	pylint --disable=R,C *.py
all:
	install lint test 
