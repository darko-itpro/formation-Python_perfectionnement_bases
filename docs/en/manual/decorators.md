# Decorators
## Closure
### General concepts
A function returned by a function retains the context in which it was created:
```python
def outer(param):
    value = param
    def inner(modif):
        return value * modif
```

You can use it this way:
```python
>>> my_answer = outer(42)
>>> my_answer(10)
420
```

### Modify the execution environment of a closure
As with any variable, variables defined in the external function are only visible in read-only for the internal function.
```python
def outer(name):
    count = 0
    def inner():
        print(f"inner func for {name}")
        nonlocal count
        count += 1
        
    return inner
```

### Accessing clusures variables
The variables defined by the external function are not accessible in the environment that retrieved the internal function. The trick is to define an accessor function attached to the returned function.

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

We can use it this way:
```python
>>> click = outer()
>>> click()
>>> click()
>>> click.get_count()
2
```

## To decorators
### General structure of a decorator
```python
def sandwich(content):
    def wrapper():
        print("/TTTTTTTTTT\\")
        content()
        print("\\__________/")
        
    return wrapper
```

Which can be called this way:
```python
def parisien():
    print("Jambon")
    print("Beurre")
    
sandwich(parisien)()
```

But also:
```python
@sandwich
def parisien():
    print("Jambon")
    print("Beurre")
```

### Passing arguments
The use of variadics allows a weak cohesion between the decorator and the function to be decorated.

```python
def sandwich(content):
    def wrapper(*args, **kargs):
        print("/TTTTTTTTTT\\")
        content(*args, **kargs)
        print("\\__________/")
        
    return wrapper
```

### Returned value

```python
def sandwich(content):
    def wrapper(*args, **kargs):
        print("/TTTTTTTTTT\\")
        value = content(*args, **kargs)
        print("\\__________/")
        
        return value
        
    return wrapper
```

### Parametrized decorators
```python
def name(key1=value1, key2=value2, ...):
    def decorator_name(func):
        ...  # La fonction wrapper
```

But this kind of decorator cannot be used without the brackets

### How to keep the *simple* syntax with parametrized decorators 
```python
def name(_func=None, *, key1=value1, key2=value2, ...):
    def decorator_name(func):
        ...  # La fonction wrapper
        
    if _func is None:
        return decorator_name
    else:
        return decorator_name(_func)
```

## Bonus: replacing the wrapper's metadata
When using a wrapper, function introspection will be *distorted*. We no longer have the original 
function, but the *wrapper* function. Test this using the `sandwich` decorator; you should get 
something similar to:
```python
>>> sandwich.__name__
'wrapper'
```

Easiest way to keep the original metadata:
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