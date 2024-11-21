import time

def cached_computation():
    cached_value = (0, 0)

    def long_call(value:int):
        nonlocal cached_value
        if value == cached_value[0]:
            result = cached_value[1]
        else:
            time.sleep(1)
            result = value ** 2
            cached_value = (value, result)

        return result

    return long_call

long_call = cached_computation()
print(long_call(2)) # 4 en 1 seconde
print(long_call(4)) # 16 en 1 seconde
print(long_call(4)) # 16 instantané