# First activity

## Introduction
With python, you can measure execution time of a code the following way:

```python
import time

start = time.perf_counter()

for x in range(1_000_000):
    y = x ** 2

end = time.perf_counter()

print(f'Executed in {end - start} seconds')
```

## Subject
Write a context manager to measure execution time of the code within the context. The context 
manager prints the elapsed time on its exit.
