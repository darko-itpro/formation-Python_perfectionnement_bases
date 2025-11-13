# Rappels - Itérations

Le projet qui vous a été fourni contient un module `pylib.datasources.pyflix` . Celui-ci contient 
la fonction `load_season(show_name, season_number)`. Cette fonction charge la saison d’une série à 
partir d’une base de données. Enfin, le simule…

Nous souhaitons gérer la notion d’épisode avec une syntaxe objet.

Déclarez un `namedtuple` qui décrit un épisode possédant les champs `title`, `season_number`, 
`number`, `duration`et `year`.

Écrivez une fonction qui retourne une liste de ces `namedtuples` à partir de l’appel à la fonction 
`pylib.datasources.pyflix.load_season(show_name, season_number)`.