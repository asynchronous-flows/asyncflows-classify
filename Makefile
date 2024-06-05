
type:
	pyright asyncflows_classify

test:
	pytest asyncflows_classify

test-no-skip:
	pytest --disallow-skip

test-fast:
	pytest -m "not slow" asyncflows_classify

lint:
	ruff check --fix

format:
	ruff format

all: format lint type test-fast
