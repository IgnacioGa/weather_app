# APP de Weather

## Configuración inicial para entorno local

### Code Style

Este repositorio utiliza [black](https://github.com/ambv/black) para formatear el codigo.

Se debe configurar la herramienta [pre-commiter](https://pre-commit.com/) ejecutando los siguientes comandos:

```
pip3 install pre-commit
pre-commit install
```

Para utilizar archivos `.envs`:

Generar y configurar el archivo `.env` en el root base del proyecto: `cp .envs/.local/.django{.dist,}`.


