# Python Playground

This is a dummy Python 3.10+ project for learning.

The starting point of this repository is based on the video from[mCoding][mCoding-channel]:
[Automated Testing in Python with pytest, tox, and GitHub Actions][mCoding-reference-video].

![Tests][github-tests-badge]

## Development setup

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -r requirements_dev.txt
```

## Run the tests locally

```shell
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements_dev.txt
tox
```

[mCoding-channel]: https://www.youtube.com/@mCoding
[mCoding-reference-video]: https://youtu.be/DhUpxWjOhME?si=myJrKVfroLfKz7Hw
[github-tests-badge]: https://github.com/m-alorda/python-playground/actions/workflows/tests.yml/badge.svg
