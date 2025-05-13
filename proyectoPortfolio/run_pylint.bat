@echo off

:: Establecer la variable de entorno DJANGO_SETTINGS_MODULE
set DJANGO_SETTINGS_MODULE=miportfolio.settings

:: Ejecutar Pylint con el plugin para Django
pylint --load-plugins pylint_django portfolio\views.py
