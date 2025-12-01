# Python, advanced training

## General information
This repository is meant for my trainings

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)
[![Static Badge](https://img.shields.io/badge/Github-Documentation-blue?logo=github)](https://darko-itpro.github.io/formation-Python_perfectionnement_bases/)

## Installation
### Working branch for the training
For the training, I will set up a dedicated branch on wich I will push all the examples and
activities.

### Get the project
The project can be anywhere you want in your folders.

### Project structure
This is a training project. It does not follow a conventional structure. The folder structure is as
follow:
 * **assets**: is a forder containing files used for data manipulation.
 * **demo**: will contain all demo files. 
 * **exos**: is your working directory for all your activities.
 * **pylib**: is a *library* project with code wich will be necessary for your programs.

## Setup
### Prerequist
[Python](https://www.python.org) must be installed on your computer. The minimal version must be 
3.10 but you should use a 3.13+.

### Development environnements
This training does not requires any specific development environment.

The suggested environments are [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/)
and [Visual Studio Code](https://code.visualstudio.com/).

Jupyter notebooks will also be used during this session.

### Project dependencies
This codebase requires some dependencies but they are not declared in a file because their 
management is part of the training. The required dependencies are listed down bellow.

## Project dependencies
This project dependencies are:
 * [ipython](https://jupyter.org/): an *advaced* interacive shell preffered over the standard one.
 * [Pytest](https://docs.pytest.org/): needed for unit testing.
 * [Pytz](https://pypi.org/project/pytz/): used for timezone management. This lib is deprecated 
   since Python 3.9 (timezones are since managed in the standard library).
 * [flake8](https://flake8.pycqa.org/): style guide enforcement tool.
 * [pylint](https://pypi.org/project/pylint/): static code analyser.
 * [jupyter-lab](https://jupyter.org/): Jupyter will be used for its notebooks for code examples and 
   documentation. This dependencie will also install the interactiver shell `ipython`.
 * [celery](https://docs.celeryq.dev/): for asynchronous tasks. Needs 
   [RabbitMQ](https://www.rabbitmq.com/) and [Redis](https://redis.io/).
 * [rich](https://github.com/Textualize/rich): let us have a *rich* text display in the terminal.
 * [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): for documentation.
 
## Additional essources

During the training, additional ressources will be available [on this shared folder](https://bit.ly/3uh2MEQ).