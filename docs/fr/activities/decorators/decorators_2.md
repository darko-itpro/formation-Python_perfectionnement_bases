# Décorateurs 2

## Sujet
Écrire un décorateur qui permet de compter le nombre d’appels à une fonction.

## Exemple
Le code suivant…
```python
@count_calls
def some_func():
    print("func called")

print(some_func.nbcalls())
some_func()
some_func()
print(some_func.nbcalls())
```

…doit donner :
```
0
func called
func called
2
```

Indice : en python, il est possible d’associer une fonction à une fonction…
Essayez.
