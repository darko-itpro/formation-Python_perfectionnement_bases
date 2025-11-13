# Troisième exercice

Écrivez un context manager qui permet de travailler temporairement dans un autre répertoire. En 
sortie du context manager, Python doit revenir dans son répertoire de travail d’avant l’appel au 
context manager.

Ainsi, vous devez pouvoir exécuter ce type de code :
```python
print(os.getcwd())

with changedir('/temp'):
    print(os.getcwd())

print(os.getcwd())
```

Qui doit vous afficher respectivement le répertoire de travail, le répertoire `/temp` puis le 
répertoire de travail.

Pour rappel, vous pouvez changer de répertoire de travail avec 
[`os.chdir(path)`](https://docs.python.org/3/library/os.html#os.chdir).