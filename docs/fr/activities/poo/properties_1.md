# Les properties, préparation

Le module `pylib.pyflix.mediatheque` contient une classe `TvShow` qui représente une série. Pour 
l’instant tous les attributs sont publics.

Votre prédécesseur n'a pas terminé l'implémentation. Commencez par vérifier la conformité des 
spécifications :

 * Le titre est un attribut du nom `name` et doit être en minuscules, la première lettre des mots en 
   capitale (il y a une méthode pour cela…).
 * La liste des épisodes est retournée par un attribut
 * Un épisode est ajoutés par la méthode `add_episode()`.
 * Ajouter un doublon doit résulter en une levée d'exception de type `DuplicateEpisode`.

Complétez également si nécessaire les autres classes du module.