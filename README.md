# Python Playground

This is a dummy Python 3.10+ project for learning.

[![Tests][github-tests-badge]][repo-home]
[![Codecov][codecov-badge]][codecov-repo]
[![Imports: isort][isort-badge]][isort-home]
[![Code style: black][black-badge]][black-home]
[![pre-commit][pre-commit-badge]][pre-commit-home]

## Development setup

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -r requirements_dev.txt
pre-commit install
```

## Run the tests locally

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements_dev.txt
tox
```

[repo-home]: https://github.com/m-alorda/python-playground
[github-tests-badge]: https://github.com/m-alorda/python-playground/actions/workflows/tests.yml/badge.svg
[codecov-repo]: https://codecov.io/gh/python-playground
[codecov-badge]: https://codecov.io/gh/python-playground/branch/main/graph/badge.svg
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-home]: https://github.com/psf/black
[isort-badge]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-home]: https://pycqa.github.io/isort/
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
[pre-commit-home]: https://github.com/pre-commit/pre-commit
