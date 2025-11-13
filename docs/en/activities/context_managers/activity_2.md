# Second activity

Write a context manager with a method `.print(str)`. This method should print the given string
indented as the recursive call.

Code example :
```python
with IndentContext() as ic:
    ic.print("One line")
    ic.print("Another line")
    with ic:
        ic.print("An indented line")
    ic.print("One more line")
```
You should get :
```
One line
Another line
    An indented line
One more line
```
