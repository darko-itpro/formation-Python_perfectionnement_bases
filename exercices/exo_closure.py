import time


def cached_calcul():
    cached_value = (None, None)

    def powerize(value):
        nonlocal cached_value
        if cached_value[0] == value:
            return cached_value[1]
        else:
            time.sleep(1)
            cached_value = (value, value**2)
        return cached_value[1]

    return powerize

popow = cached_calcul()
print(popow(3))
print(popow(5))
print(popow(5))
print(popow(12))