# AWS Tagging Orchestrator

This project aims to provide a container that can be used to tag AWS resources in an account based on configuration.

## Development

### Prerequisites

- [Python 3.12](https://www.python.org/downloads/)
- [Poetry 1.8.2](https://python-poetry.org/docs/#installation)

### Setup

Run the following command to install the dependencies:

```bash
# Install dependencies
poetry config virtualenvs.in-project true
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install
```

### Running the tests

Run the following command to run the tests:

```bash
poetry run pytest --cov='aws_tagging_orchestrator' . -n 2 --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report html --cov-report term-missing --cov-fail-under 50
```
