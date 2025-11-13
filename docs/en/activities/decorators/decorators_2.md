# Decorators 2

## Subject
Write a decorator which will count the number of calls of the function

## Exemple
The following code…
```python
@count_calls
def some_func():
    print("func called")

print(some_func.nbcalls())
some_func()
some_func()
print(some_func.nbcalls())
```

…must display:
```
0
func called
func called
2
```

Hint: in Python, you can attach a function to another function. Try it.
