# Rappels - itérations

Pour cet exercice, vous utiliserez le module `pylib.datasources.pyacademy`. Celui-ci contient deux 
fonctions, `load_students_list()` et `load_grades(course:str)`.

`load_students_list()` retourne une liste d’étudiants

`load_grades(course:str)` prend en paramètre les valeurs `math` ou `english` et retourne la liste 
des notes pour cette matière. Toute autre argument lèvera une exception.

Il est considéré que les fonctions retournent les données dans le même ordre (une note en position 
i du retour de la fonction `load_grades(course:str)` correspond à la note de l’élève en position i 
du retour de la fonction `load_students_list()`).

Itérez sur les trois collections (étudiants, notes de math et notes d’anglais) pour afficher les 
élèves avec leur notes.

Construisez un dictionnaire dont la clef sera le nom de l’élève et la valeur sera la liste de ses 
notes (maths en première position, anglais en seconde).