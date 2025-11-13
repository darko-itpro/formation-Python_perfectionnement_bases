# Les closures

Nous allons écrire une fonction qui simule faire quelque chose de « long ». Soit donc la fonction 
suivante.

```python
import time

def long_call(value:int):
    time.sleep(2)
    return value**2
```

Cette fonction ne calcule que le carré du paramètre mais son temps d'exécution est de 2 secondes.

## Exercice

Modifiez cette fonction afin que si elle est appelée avec l’argument précédent, elle "ne refait pas 
le calcul" mais utilise la valeur en cache.

## Évolution

Étendez la fonctionnalité pour toutes les valeurs précédentes.