# Les décorateurs
## Notion de Closure
### Généralités
Une fonction retournée par une fonction retient le contexte dans lequel elle a été créée :
```python
def outer(param):
    value = param
    def inner(modif):
        return value * modif
```

Va s'utiliser :
```python
>>> my_answer = outer(42)
>>> my_answer(10)
420
```

### Modifier l'environnement d'exécution d'une closure
Comme pour toute variable, les variables définis dans la fonction externe ne sont visibles qu'en lecture seule pour la fonction interne.
```python
def outer(name):
    count = 0
    def inner():
        print(f"inner func for {name}")
        nonlocal count
        count += 1
        
    return inner
```

### Accéder aux variables de l'environnement d'exécution
Les variables définies par la fonction externe ne sont pas accessibles dans l'environnement qui a récupéré la fonction interne. L'astuce consiste à définir une fonction accesseur attachée à la fonction retournée.

```python
def outer(name):
    count = 0
    
    def inner():
        print(f"inner func for {name}")
        nonlocal count
        count += 1
        
    def inner_get_count():
        return count
        
    inner.get_count = inner_get_count
    
	return inner
```

Nous pouvons alors utiliser :
```python
>>> click = outer()
>>> click()
>>> click()
>>> click.get_count()
2
```

## Vers les décorateurs
### Structure générale des décorateurs
```python
def sandwich(content):
    def wrapper():
        print("/TTTTTTTTTT\\")
        content()
        print("\\__________/")
        
    return wrapper
```

Ce qui peut s'appeler de la manière suivante :
```python
def parisien():
    print("Jambon")
    print("Beurre")
    
sandwich(parisien)()
```

Mais aussi
```python
@sandwich
def parisien():
    print("Jambon")
    print("Beurre")
```

### Passage d'arguments

L'usage de variadics permet une cohésion faible entre le décorateur et la fonction à décorer.

```python
def sandwich(content):
    def wrapper(*args, **kargs):
        print("/TTTTTTTTTT\\")
        content(*args, **kargs)
        print("\\__________/")
        
    return wrapper
```

### Valeur en retour

```python
def sandwich(content):
    def wrapper(*args, **kargs):
        print("/TTTTTTTTTT\\")
        value = content(*args, **kargs)
        print("\\__________/")
        
        return value
        
    return wrapper
```

### Décorateur paramétré
```python
def name(key1=value1, key2=value2, ...):
    def decorator_name(func):
        ...  # La fonction wrapper
```

Mais ceci fait que le décorateur ne peut être utilisé sans parenthèses.

### Conserver la syntaxe simple avec le décorateur paramétré 
```python
def name(_func=None, *, key1=value1, key2=value2, ...):
    def decorator_name(func):
        ...  # La fonction wrapper
        
    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)
```

## Bonus : remplacer les métadonnées du wrapper
Dans le cas de l'utilisation d'un wrapper, l'introspection de la fonction sera *faussé*. Nous n'avons plus la fonction d'origine mais la fonction wrapper. Faites le test sur la base du décorateur `sandwich`, vous devriez avoir quelque chose de similaire à :
```python
>>> sandwich.__name__
'wrapper'
```

Pour préserver les informations de la fonction d'origine :
```python
import functools

def sandwich(content):
    @functools.wraps(content)
    def wrapper():
        print("/TTTTTTTTTT\\")
        content()
        print("\\__________/")
        
    return wrapper
```