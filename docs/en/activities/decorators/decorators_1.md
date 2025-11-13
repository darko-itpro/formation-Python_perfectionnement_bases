# Decorators 1

## Introduction
With python, you can measure execution time of a code the following way:

```python
import time

start = time.time()

for x in range(1_000_000):
    y = x ** 2

end = time.time()

print(end - start, "seconds")
```
## Subject
Write a decorator to measure execution time of the code within the context. The decorator prints 
the elapsed time.

## Sujet
Écrivez un décorateur qui permet de mesurer le temps d’exécution d’une fonction. Le décorateur 
devra simplement afficher le temps d’exécution.