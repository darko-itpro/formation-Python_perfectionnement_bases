# Iterators

An **iterator** is an object that *returns* the next element of an **iterable**. The most common 
iterables are sequences or generators.

An **iterable** object is an object that implements `__iter__`, which is expected to return an 
iterator object. An **iterator** object implements `__next__`, which is expected to return the next 
element of the iterable or raise a `StopIteration` when no more elements are available.
