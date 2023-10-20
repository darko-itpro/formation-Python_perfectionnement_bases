
def coroutine(func):
    """
    Décorateur de générateurs utilisés en coroutines.
    """
    def starter(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    # Les lignes suivantes permettent de redéfinir la fonction starter qui sera retournée
    # avec le nom de la fonction décorée.
    s = starter
    s.__name__ = func.__name__

    return s