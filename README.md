# Future Cities CCT - FCSA Document 

Foobar is a Python library for dealing with word pluralization.

## Technology Stack:
* FastAPI
* Uvicorn (server)
* Pytest
* JinJa2
* GitHub
* Jenkins (Testing)
* Pytest-harvest

## Poetry  
- python is dependency management
- Dependency Management Tool.
- Commands to manage, setup, run and deploy a project

## Poetry Installation:
On Linux/bash on windows
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python –
```
On windows PowerShell
```
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python –
```
## Using pip

To install poetry on your local system. You can also install it using pip which is not recommended method
```bash
pip install poetry
```
To verify if poetry is installed or not:
```bash
poetry --version
```
#Activating virtual environment

Poetry creates its own virtual environment at the time of installation so that it won’t mess with other programs in your system. 
To activate the virtual environment in your project you simply need to type this command :

```bash
poetry shell
```

## How to add new Dependencies:

```python
poetry add fastapi
```
```python
poetry add requests
```
## How to run Python scripts with Poetry:

```python
poetry run python main.py
```

#### Poetry - generate requirements.txt without hashes
```python

poetry export --without-hashes --format=requirements.txt > requirements.txt
```

```
## License
[MIT](https://choosealicense.com/licenses/mit/)