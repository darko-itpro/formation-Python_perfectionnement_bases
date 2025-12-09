# Les context managers
## Structure de base

```python
class BasicContextManager:
    def __enter__(self):
        print("Entering Context Manager")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context Manager")

```

Usage :

```python
with BasicContextManager():
    print('In context')
```

## Un context manager reste un objet
Le contexte manager reste une classe et donc un objet. IL peut avoir une méthode `__init__(self)`

```python
class BasicContextManager:
    def __init__(self):
        print("Initializing")
        self.my_id = "I'm the context"
        
    def __enter__(self):
        print("Entering Context Manager")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context Manager")

```

```python
bc = BasicContextManager()
with bc:
    print(f'In context {bc.my_id}')
```

## Idiome with as
Le mot clef as récupère le retour de la fonction `__enter__(self)`.

```python
class BasicContextManager:
    def __init__(self):
        print("Initializing")
        self.my_id = "I'm the context"
        
    def __enter__(self):
        print("Entering Context Manager")
        return self

```

Permet l'usage :
```python
with BasicContextManager() as bc:
    print(f'In context {bc.my_id}')
```

## Gestion des exceptions
### Paramètres de `__exit__()`
Si une exception se produit dans le contexte et l’interrompt, elle peut être gérée dans la méthode `__exit__()`. Les paramètres de cette méthodes vont alors entrer en jeu. La signature complète de la méthode est `__exit__(self, exc_type, exc_value, exc_tb)`.
 * **exc_type** : est le type (classe) de l’exception
 * **exc_value** : est l’instance de l’exception
 * **exc_tb** : est l’objet _traceback_

**Attention**, vous ne devez pas lever une exception dans ce bloc pour faire suivre l’exception.

### Propagation de l'exception
Si vous avez géré l’exception et qu’elle ne doit pas être propagée, alors la méthode doit retourner une valeur **vrai** (**truthy**). Si la méthode retourne une valeur **falsy** (ce qui est fait par défaut puisque le retour est `None`), l’exception sera propagée.