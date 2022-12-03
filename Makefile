run:
	python3 src/main.py

unit-tests:
	python3 -m unittest test/unit-test.py -v

integration-tests:
	python3 -m unittest test/integration-test.py -v


setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf src/__pycache__