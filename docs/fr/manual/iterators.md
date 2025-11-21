# Les itérateurs

Un **itérateur** est un objet qui permet de retourner le prochain élément d’un **itérable**. Les 
exemples les plus simples d’itérateurs sont les séquences mais aussi les générateurs.

Un **itérable** est un objet implantant la méthode spéciale `__iter__`  qui doit retourner un 
itérateur. Un **itérateur** est un objet implantant la méthode spéciale `__next__`. Cette méthode 
doit retourner l’élément suivant ou lever une exception de type `StopIteration`.
