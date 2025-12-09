# Programmation Orientée Objet Avancée
## Les properties 
Les properties permettent d'exposer un attribut tout en contrôlant sa modification. Ils permettent de renforcer le principe d'encapsulation consistant à masquer l'implémentation.
Rappelez-vous qu'une propertie ne se limite pas à un *passe-plat* vers un attribut *privé*.

Soit une propertie `prop` d’une classe `MyClass` instanciée en `my_object`.
### Utilisation sous forme de décorateur
#### Déclaration de l’accesseur (getter)
```python
class MyClass:

@property
def prop(self):
    return value
```

L'appel se fera par :
```python
my_object = MyClass()
my_object.prop
```

#### Déclaration du mutateur (setter)
```python
class MyClass:

@property
def prop(self):
    return value
    
@prop.setter
def prop(self, new_value)
    self.value = new_value
```

L'appel se fera par :
```python
my_object = MyClass()
my_object.prop = value
```

#### Déclaration du suppresseur (deletter)
```python
class MyClass:

@property
def prop(self):
    return value
    
@prop.deletter
def prop(self)
    pass
```
Le suppresseur sera appelé lors des instructions de type :
```python
my_object = MyClass()
del my_object.prop
```

### Implémentation réelle d'une property

```python
class MyClass:

def _get_value(self):
    return self.value
    
def _set_value(self, new_value)
    self.value = new_value
    
def _del_value(self):
    pass

prop = property(_get_value, _set_value, _del_value)
```

---
## Ajouter fonctionnalités de *conteneur* à une classe
### Taille du conteneur
```python
class MyClass:
    def __len__(self):
        return 42 # Doit retourner un entier
```

Usage :
```python
len(my_object)
```

### Interroger sur la présence d'un élément
```python
class MyClass:
    def __contains__(self, item):
    return True
```

Usage :
```python
value in my_object
```

### Accéder  à un élément par sélection
En anglais, on utilise le terme de *subscripting* dont la traduction est *sélection* ou *indiçage*. Il permet d'accéder à un élément d'une collection par indice ou clef en fonction des cas d'usage.

Trois metodes permettent d'accéder, modifier ou supprimer un élément par sélection.
```python
class MyClass:
    def __getitem__(self, key):
        return value
        
    def __setitem__(self, key, new_value):
        self.value_from_key = new_value
        
    def __delitem__(self, key):
        pass
```

Usages :
```python
my_object[element_id]
my_object[element_id] = value
del my_object[element_id]
```

---
