# Décorateurs 1

## Introduction
En Python, il est possible de mesurer la durée d’exécution d’un code de la manière suivante :

```python
import time

start = time.perf_counter()

for x in range(1_000_000):
    y = x ** 2

end = time.perf_counter()

print(f'{end - start} secondes se sont écoulées')
```

## Sujet
Écrivez un décorateur qui permet de mesurer le temps d’exécution d’une fonction. Le décorateur 
devra simplement afficher le temps d’exécution.