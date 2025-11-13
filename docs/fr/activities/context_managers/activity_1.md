# Premier exeercice

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
Écrivez un context manager qui permet de mesurer l’exécution du code dans le contexte. En sortie du 
context, le context manager affiche la durée d’exécution.