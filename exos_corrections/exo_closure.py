import time
from collections import OrderedDict

def cached_computation():
    cached_value = OrderedDict()

    def long_call(value:int):
        try:
            result = cached_value[value]
            cached_value.move_to_end(value)
        except KeyError:
            time.sleep(1)
            result = value ** 2
            cached_value[value] = result
            if len(cached_value) > 5:
                print(cached_value.popitem(last=False))

        return result

    return long_call

long_call = cached_computation()
print(long_call(2)) # 4 en 1 seconde
print(long_call(4)) # 16 en 1 seconde
print(long_call(4)) # 16 instantané
print(long_call(2)) # 4 en 1 seconde
print(long_call(5))
print(long_call(6))
print(long_call(7))
print(long_call(8))