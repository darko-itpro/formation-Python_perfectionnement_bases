# Formation Python Perfectionnement

🇬🇧 [English version here](README_en.md) 🇬🇧

## Généralités

Ce référentiel complète la formation Python Perfectionnement que je propose et est donc destiné à
mes stagiaires.

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)
[![Static Badge](https://img.shields.io/badge/Github-Documentation-blue?logo=github)](https://darko-itpro.github.io/formation-Python_perfectionnement_bases/)

La [documentation GitHub](https://darko-itpro.github.io/formation-Python_perfectionnement_bases/) est disponible.

Ces sources sont organisées pour proposer des exemples de code sur les thèmes couverts par les
formations Python Perfectionnement. Elles respectent avec quelques adaptations l'organisation d'un
package *flat*.

## Procédure d'installation
### Branche dédiée à la formation
Pour mes formations, je prépare une branche dédiée à laquelle j'ajoute les illustrations et les
corrections d'exercices. Faites donc attention aux potentiels conflits. 

### Récupérez le projet
Le projet peut être dans l'arborescence que vous souhaitez sur votre disque. Vous pouvez soit cloner
le projet soit le récupérer sous forme d'une archive.

Si vous récupérez le projet sous forme d'une archive, vous êtes indépendants du référentiel de
sources. Vous pourrez récupérer les corrections sous forme d'une autre archive.

Si vous clonez le projet, il y aura le risque d'un conflit. L'idéal sera de créer votre branche de
travail.

## Structure du projet
Ce projet est un projet de formation. Sa structure ne suit donc pas la
structure conventionnelle d'un projet Python. L'organisation des répertoires
est la suivante :
 * `assets` : est un répertoire contenant des fichiers qui seront nécessaires
 pour le parcours et la manipulation de fichiers.
 * `demos` : est un package contenant des fichiers de démonstration et d'illustration.
 * `docs`: contient la documentation qui est déployée comme [pagees GitHub](https://darko-itpro.github.io/formation-Python_perfectionnement_bases/).
 * `exos` : est votre répertoire de travail. Il est destiné à contenir le
 code que vous allez produire durant la formation et vous permettre de le
 retrouver dans cet emplacement unique.
 * `src`: Répertoire du contenu déployé (voir ci-dessous) contenant les packages suivants :
   * `pylib` : est un répertoire contenant du code qui sera utilisé par vos
   programmes.

## Mise en place de l'environnement

### Prérequis
[Python](https://www.python.org) doit être installé sur votre poste.

La formation est prévue pour une version de Python 3.10+.

### Environnements de développement
Ce code ne nécessite aucun IDE en particulier.

Les environnements conseillés sont [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/)
et [Visual Studio Code](https://code.visualstudio.com/).

Une partie de la formation peut reposer sur des notebooks Jupyter.

### Installation de dépendances
Ce projet utilise les pratiques _modernes_. Bien qu'historiquement les dépendances soient déclarées 
dans les fichiers `requirements.txt`, pour ce projet, elles sont dans le `pyproject.toml`.

Les instructions sont donc :

Pour installer le projet (le contenu du répertoire `src`) en mode éditable :
```bash
pip install -e .
```

Depuis la version **26.2** de `pip`, vous pouvez installer uniquement les dépendances du projet 
avec :

```bash
pip install . --only-deps
```

Pour installer les dépendances de _dév'_ :

```bash
pip install --group dev
```

Certaines dépendances sont déclarées comme _optionnelles_. Il s'agit de `Celery` et de son 
interface web `flower`. Elles sont contenues dans le nom `[tasking]`.

Dans le contexte de la formation, pour une installation en mode éditable, l'instruction pour les 
installer est :

```bash
pip install -e ".[tasking]"
```
 
### Makefile
Si vous êtes sur un environnement POSIX (Linux ou MacOs) ou plus généralement si vous utilisez
l'outil `make`, vous pouvez utiliser le `makefile` fourni :

 * `make clean` : supprime les répertoires et les fichiers créés par les autres commandes ou lors 
   des exécutions (comme l'arborescence du _site_).
 * `make doc-build` : génère la documentation en local. 
 
## Dépendances du projet
Les dépendances utilisées pour cette formation sont les suivantes.

### Dépendances _de production_

Il s'agit des dépendances indispensables pour le bon fonctionnement du projet.

 * [ipython](https://jupyter.org/) : il s'agit d'un shell intéractif avancé encore préféré au shell
   intéractif standard.
 * [jupyter-lab](https://jupyter.org/) : sera utilisé pour ses notebooks, documents
   d'illustration. Cette dépendance installera également le shell intéractif 
   avancé `ipython`. `Jupyter-lab` est une évolution du projet `Jupyter`.
 * [rich](https://github.com/Textualize/rich) : permet d'avoir un texte *riche* dans le terminal.
 * [platformdirs](https://pypi.org/project/platformdirs/) : utilisé pour déterminer les répertoires 
   utilisateur en fonction de la plate-forme.

### Dépendances _de développement_

Il s'agit des dépendances nécessaires pour le développement mais qui ne doivent pas être installées 
en prod.

 * [Pytest](https://docs.pytest.org/) : utilisé pour la partie tests unitaires
 * [Pytz](https://pypi.org/project/pytz/) : utilisé pour la gestion des TimeZone des dates. Bien
   que dépréciée depuis Python 3.9, elle est présente à but d'illustration d'une
   dépendance *de prod* 
 * [flake8](https://flake8.pycqa.org/) : outil de validation statique de code
 * [pylint](https://pypi.org/project/pylint/) : outil d'analyse statique de code
 * [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) pour la documentation.

### Dépendances _Optionnelles_

Les dépendances suivantes ne sont pas indispensables au projet si on n'utilise pas leurs 
fonctionalités.

 * [celery](https://docs.celeryq.dev/) : utilisé pour l'asynchronisme. Nécessite
   [RabbitMQ](https://www.rabbitmq.com/) et [Redis](https://redis.io/).
 
## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://bit.ly/3uh2MEQ)
