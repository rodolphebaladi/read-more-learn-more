run:
	python3 src/main.py

unit-tests:
	python3 -m unittest test/unit-test.py -v

integration-tests:
	python3 -m unittest test/integration-test.py -v


performance-tests:
	python3 -m unittest test/performance-test.py

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf src/__pycache__
