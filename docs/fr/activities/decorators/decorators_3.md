# Décorateurs 3

## Présentation
Nous allons écrire une fonction qui simule faire quelque chose de « long ». Soit donc la fonction 
suivante.

```python
def long_call(value:int):
    time.sleep(2)
    return value**2
```

Cette fonction ne calcule que le carré du paramètre mais son temps d'exécution est de 2 secondes.

## Sujet
Créez un décorateur qui permet de mettre la valeur calculée en cache. Si la fonction est rappelée 
avec la valeur qui vient d'être calculée, elle ne refait pas le calcul mais retourne la valeur en 
cache.

## Évolution
Améliorez le décorateur pour permettre à plusieurs valeurs d'être mises en cache.
