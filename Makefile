PYTHON = python3
TESTS = tests.py

tests:
	$(PYTHON) $(TESTS)

clean:
	rm -r -f logs/*

	clear

	@echo "Cleaned!"

deep_clean:
	rm -r -f __pycache__/
	make clean
