# utencilos

A collection of useful code for working with data. "Utencilos" is the spanish word for utensils.

### Dev Tips

To install package in dev mode to venv:
```
$ pip install -e .
```

To create distribution archives
```
$ python3 -m pip install --upgrade build
$ python3 -m build
```

To upload package to test pypi
```
$ python3 -m twine upload -r testpypi dist/*
```

To run tests (after activating the virtual environment)
```
$ python -m pytest
```

https://packaging.python.org/en/latest/