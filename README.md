# Weather App

## Stack

- Django
- HTMX
- Tailwind
- Hyperscript

## Initial configuration for local development

### Code Style

This project provides a complete configuration for flake8, isort and black. Between these three tools, consistent quality code can be ensured

We need to configurate the pre commiter tool [pre-commiter](https://pre-commit.com/) running this commands:

```
pip3 install pre-commit
pre-commit install
```

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:IgnacioGa/weather_app.git
$ cd weather_app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Then we have to migrate the database:

```sh
(env)$ cd weather_app
(env)$ python manage.py migrate
```

Once `pip` has finished downloading the dependencies and the migrate finish:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Frontend

In order to make tailwind and general frontend changes we need to start it

```sh
(env)$ python manage.py tailwind start
```

This will keep the track of the changes in the theme apps, where are the custom class and the tailwind configuration

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test
```

Deployed app -> https://weather-app-gallo.up.railway.app/
