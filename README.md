#  Locust Template

This project contains boiler plate that I can use for starting new Locust projects in the future.


### Pre-Requisite
To run this project you need poetry install on your machine. To install run:
```bash
brew install pipx

pipx install poetry
```
> **Note:** Installation via pipx is the reccomended poetry installation path.

# Setting Up Local Dependencies

This project currently only runs locally. For packagement, the project uses the Poetry. Poetry is a Python package, venv, and project manager. ONce you have cloned the repo you can install all
dependencies by running:
```bash
poetry install
```

You can then enter the venv by running:
```bash
poetry shell
```

## Sensitive Credentials
This project uses **dotenv** for managing sensitive credentials locally. If you look in `settings.py` you will see that series of sensitive creds are pulled-in via env vars. You can create a `.env` file in the `LoadTests/` dir and populate it with the values you want for those as so:
```bash
USERNAME="<Your username>"
PASSWORD="<Your password>"
```


Launch the WebUI with:
```bash
cd LoadTests/
locust WebsiteUser
```


