run:
	python3 src/main.py

testing:
	python3 test/test.py

#setup: requirements.txt
#    pip install -r requirements.txt

clean:
	rm -rf src/__pycache__