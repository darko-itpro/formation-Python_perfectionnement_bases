# Formation Python Perfectionnement
## Généralités

This is the practical cases for Python training I provide. Intended for french trainee, the rest
of the explanations are in french.

Ce référentiel complète la formation Python Perfectionnement que je propose et est donc destiné à
mes stagiaires.

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)
[![Static Badge](https://img.shields.io/badge/Github-Documentation-blue?logo=github)](https://darko-itpro.github.io/formation-Python_perfectionnement_bases/)

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
 * **assets** : est un répertoire contenant des fichiers qui seront nécessaires
 pour le parcours et la manipulation de fichiers.
 * **demos** : est un package contenant des fichiers de démonstration et d'illustration.
 * **exos** : est votre répertoire de travail. Il est destiné à contenir le
 code que vous allez produire durant la formation et vous permettre de le
 retrouver dans cet emplacement unique.
 * **pylib** : est un répertoire contenant du code qui sera utilisé par vos
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
Les dépendances nécessaires au projet ne sont pas déclarées car la création
d'un fichier requirements fait parti de ces formations. Les dépendances
nécessaires sont listées ci-après.
 
## Dépendances du projet
Les dépendances suceptibles d'être utilisées pour cette formation sont les
suivantes :
 * [ipython](https://jupyter.org/) : il s'agit d'un shell intéractif avancé encore préféré au shell
   intéractif standard.
 * [Pytest](https://docs.pytest.org/) : utilisé pour la partie tests unitaires
 * [Pytz](https://pypi.org/project/pytz/) : utilisé pour la gestion des TimeZone des dates. Bien
   que dépréciée depuis Python 3.9, elle est présente à but d'illustration d'une
   dépendance *de prod* 
 * [flake8](https://flake8.pycqa.org/) : outil de validation statique de code
 * [pylint](https://pypi.org/project/pylint/) : outil d'analyse statique de code
 * [jupyter](https://jupyter.org/) : Jupyter sera utilisé pour ses notebooks, documents
   d'illustration. Cette dépendance installera également le shell intéractif 
   avancé `ipython`.
 * [jupyter-lab](https://jupyter.org/) : est une évolution du projet Jupyter. Normalement on
   utilise l'un ou l'autre. Les deux sont présents dans le contexte de formation.
 * [celery](https://docs.celeryq.dev/) : utilisé pour l'asynchronisme. Nécessite
   [RabbitMQ](https://www.rabbitmq.com/) et [Redis](https://redis.io/).
 * [rich](https://github.com/Textualize/rich) : permet d'avoir un texte *riche* dans le terminal.
 * [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) pour la documentation.
 
## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://bit.ly/3uh2MEQ)
