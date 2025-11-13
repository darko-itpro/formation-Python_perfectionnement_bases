# Closures

We are going to use a function that simulates something *long*.

```python
import time

def long_call(value:int):
    time.sleep(2)
    return value**2
```

This function calculates the square of the value but takes 2 seconds for that.

## Activity
This function should be faster if called a second time with the same argument.

Modify that function so that on each call she stores the result. If she's called a second time with 
the same argument, she retunes the cached value instead of calculating it again. 

## Improvement
Extend the feature for all previous values.
