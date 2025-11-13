# Décorateurs 01

## Introduction
En Python, il est possible de mesurer la durée d’exécution d’un code de la manière suivante :

```python
import time

start = time.time()

for x in range(1_000_000):
    y = x ** 2

end = time.time()

print(end - start, "secondes se sont écoulées")
```

## Sujet
Écrivez un décorateur qui permet de mesurer le temps d’exécution d’une fonction. Le décorateur 
devra simplement afficher le temps d’exécution.