# Les itérateurs

## Définitions
Un **itérateur** est un objet qui permet de retourner le prochain élément d’un **itérable**. Les 
exemples les plus simples d’itérateurs sont les séquences mais aussi les générateurs.

Un **itérable** est un objet implantant la méthode spéciale `__iter__`  qui doit retourner un 
itérateur. Un **itérateur** est un objet implantant la méthode spéciale `__next__`. Cette méthode 
doit retourner l’élément suivant ou lever une exception de type `StopIteration`.

## Itération sur une collection
Principe de base :
```python
class MyClass:
    def __iter__(self):
        self._current_value = 0
        return self
	    
    def __next__(self):
        try:
            value = self.students[self._current_value]
            self._current_value += 1
            return value
        except IndexError:
            raise StopIteration("End of collection")
```
