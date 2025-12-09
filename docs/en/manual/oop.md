# Advanced Object Oriented Programming
## Properties 
Properties allow you to expose an attribute while controlling its modification. They reinforce the 
principle of encapsulation, which consists of hiding the implementation. Remember that a property 
is not limited to expose a *private* attribute.

Consider a property `prop` of a class `MyClass` instantiated in `my_object`.
### Usage as decorators
#### The accessor (getter)
```python
class MyClass:

@property
def prop(self):
    return value
```

Will be called as:
```python
my_object = MyClass()
my_object.prop
```

#### The mutator (setter)
```python
class MyClass:

@property
def prop(self):
    return value
    
@prop.setter
def prop(self, new_value)
    self.value = new_value
```

Will be called as:
```python
my_object = MyClass()
my_object.prop = value
```

#### The suppressor (deletter)
```python
class MyClass:

@property
def prop(self):
    return value
    
@prop.deletter
def prop(self)
    pass
```

The suppressor will be called by this king of expression:
```python
my_object = MyClass()
del my_object.prop
```

### *Real* implementation of a property

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
## Emulating container types
### Size of the container
```python
class MyClass:
    def __len__(self):
        return 42 # Doit retourner un entier
```

Usage:
```python
len(my_object)
```

### Membership test
```python
class MyClass:
    def __contains__(self, item):
    return True
```

Usage:
```python
value in my_object
```

### subscripting
There are three methods for accessing, modifying, or deleting an item by selection.
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
