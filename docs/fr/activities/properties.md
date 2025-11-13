# Les properties

Le module `pylib.pyflix.mediatheque` contient une classe `TvShow` qui représente une série. Pour 
l’instant tous les attributs sont publics.

Commencez par vérifier la conformité des spécifications :

 * Le titre est un attribut du nom `name` et doit être en minuscules, la première lettre des mots en 
   capitale.
 * La liste des épisodes est retournée par un attribut
 * Un épisode est ajoutés par la méthode `add_episode()`.
 * Ajouter un doublon doit résulter en une exception.

Ensuite, vous devrez vous assurer que :

 * la liste des épisodes ne doit pas être modifiée par son attribut, uniquement en ajoutant un 
   épisode par la méthode.
 * Si le titre est modifié par l’affectation à l’attribut, la casse doit être respectée
 * Nous devons pouvoir obtenir la durée de la série par une syntaxe d’attribut.

Complétez également si nécessaire les autres classes du module.