
def coroutine(func):
    """
    Decorator generators acting as coroutines.
    """
    def starter(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    s = starter
    s.__name__ = func.__name__

    return s