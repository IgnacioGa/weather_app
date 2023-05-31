# APP de Weather

## Configuración inicial para entorno local

### Code Style

Este repositorio utiliza [black](https://github.com/ambv/black) para formatear el codigo.

Se debe configurar la herramienta [pre-commiter](https://pre-commit.com/) ejecutando los siguientes comandos:

```
pip3 install pre-commit
pre-commit install
```

Create a .env file containing any settings you want set in the container environment. At a minimum, you will need to set DATABASE_URL. Copying .env.sample will give you good starting point configured for the default database.


# APP de Weather

### Code Style

This project provides a complete configuration for flake8, isort and black. Between these three tools, consistent quality code can be ensured

Se debe configurar la herramienta [pre-commiter](https://pre-commit.com/) ejecutando los siguientes comandos:

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

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd weather_app
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