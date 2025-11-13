# Second exercice

Écrire un contexte manager qui contient une méthode `.print(str)`. Celle-ci affiche la chaine de 
caractères passée en paramètre en l’indentant en fonction de l’appel récursif du contexte manager.

Exemple de code :
```python
with IndentContext() as ic:
    ic.print("une ligne")
    ic.print("une autre ligne")
    with ic:
        ic.print("une ligne indentée")
    ic.print("une autre ligne")
```
Doit  donner une sortie comme ceci :
```
une ligne
une autre ligne
    une ligne indentée
une autre ligne
```
