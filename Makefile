.DEFAULT_GOAL := check

.PHONY: install lint lint-fix format type-check test test-cov check clean

install:
	uv sync --dev

lint:
	uv run ruff check .
	uv run ruff format --check .

lint-fix:
	uv run ruff check --fix .
	uv run ruff format .

format:
	uv run ruff format .

type-check:
	uv run mypy zamp_sdk

test:
	uv run pytest

test-cov:
	uv run pytest --cov=zamp_sdk --cov-report=xml --cov-report=term-missing

check: lint type-check test

clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache coverage.xml dist build *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
