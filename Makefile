PYTHON = python3
TESTS = tests.py

tests:
	$(PYTHON) $(TESTS)

clean:
	rm -r __pycache__/
	rm -r logs/

	clear

	echo "Cleaned!"
