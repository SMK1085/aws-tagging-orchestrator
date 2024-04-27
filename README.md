# AWS Tagging Orchestrator

![github actions workflow](https://github.com/SMK1085/aws-tagging-orchestrator/actions/workflows/main.yaml/badge.svg)
![codecov](https://codecov.io/gh/SMK1085/aws-tagging-orchestrator/graph/badge.svg?token=ZlGLbiiRKL)
![Known Vulnerabilities](https://snyk.io/test/github/SMK1085/aws-tagging-orchestrator/badge.svg)

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

#### Codecov Coverage

The following graph shows the current project [coverage](https://codecov.io/gh/SMK1085/aws-tagging-orchestrator):

![Coverage](https://codecov.io/gh/SMK1085/aws-tagging-orchestrator/graphs/sunburst.svg?token=ZlGLbiiRKL)
