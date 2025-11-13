# Context managers

## Basic structure

```python
class BasicContextManager:
    def __enter__(self):
        print("Entering Context Manager")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context Manager")

```

Usage:

```python
with BasicContextManager():
    print('In context')
```

## A context manager is an object
A context manager is a class and so, an object. It can have a `__init__(self)` method.

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
The keyword `as` gets the return of the `__enter__(self)` method.

```python
class BasicContextManager:
    def __init__(self):
        print("Initializing")
        self.my_id = "I'm the context"
        
    def __enter__(self):
        print("Entering Context Manager")
        return self

```

Let us write:
```python
with BasicContextManager() as bc:
    print(f'In context {bc.my_id}')
```

## Exceptions management
### `__exit__()` parameters
Exceptions thrown in the context can be managed in the `__exit__()` method.

The method parameters will be of use there. The entire signature 
is `__exit__(self, exc_type, exc_value, exc_tb)`.

 * **exc_type** : is the exception type (class)
 * **exc_value** : is the exception instance (object)
 * **exc_tb** : is a _traceback_ object

**Warning**, you shouldn't rise an exception in the exit method.

### Exception propagation
If you have managed the exception and it shouldn't be propagated, the method must return 
a **truthy** value. If the method returns a **falsy** value, which is the default as it returns 
`None`, the exception is propagated up.
