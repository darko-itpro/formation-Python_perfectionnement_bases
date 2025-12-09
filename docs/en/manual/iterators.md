# Iterators

## Definitions
An **iterator** is an object that *returns* the next element of an **iterable**. The most common 
iterables are sequences or generators.

An **iterable** object is an object that implements `__iter__`, which is expected to return an 
iterator object. An **iterator** object implements `__next__`, which is expected to return the next 
element of the iterable or raise a `StopIteration` when no more elements are available.

## Iterating over a collection
Basic principle:
```python
class MyClass:
    def __iter__(self):
        self._current_value = 0
        return self
	    
    def __next__(self):
        try:
            value = self.students[self._current_value]
            self._current_value += 1
            return value
        except IndexError:
            raise StopIteration("End of collection")
```
