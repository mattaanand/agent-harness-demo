PYTHON ?= $(shell test -x .venv/bin/python && echo .venv/bin/python || echo python3)

.PHONY: check lint test
check: lint test

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest -q
