# house-plant-hub-api
API containing backend logic to handle moisture readings from sensors across my house. Exposes endpoints to allows NodeMCU ESP8266 to add moisture data to the database, and then a Frontend to display the data.

## Requirements
- Python 3.10.8+

## Endpoints

### POST input_reading/

The following query must be made for the `input_reading/` command:

`<origin>api/v1/input_reading/?moisture_level=<moisture level value>`

The following headers must be provided:
- `Plant-ID`
- `Authorization`: Value must be: `API-Key <API key value>`

## Creating and Starting a Virtual Environment

Best way to download the required python packages and run the app locally is to start a virtual environment

```bash
pip install virtualenv
python -m venv .venv
source .venv/bin/activate
```

## Downloading Required Libraries

```bash
poetry shell
poetry install
```

## Running API Locally

Run locally:
```bash
./manage.py runserver 0.0.0.0:800
```

## Running Static Analysis

```bash
flake8
```

## Committing Changes to Repository

Create new branch from release branch:
```bash
git checkout -b feat/<branch name>
```

Committing branch changes (must start with `feat:` or `fix:`):
```bash
git add .
git commit -m "<commit message>"
git push
```

Adding new Python libraries:

1. Add library to `pyproject.toml`
2. run `poetry lock` to add to `poetry.lock` file
3. run `poetry export --without-hashes --format=requirements.txt > requirements.txt` to add to `requirements.txt` file
