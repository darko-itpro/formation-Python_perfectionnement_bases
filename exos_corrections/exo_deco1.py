import time

def time_it(func):
    def wrapper(*args, **kargs):
        start = time.process_time()
        value = func(*args, **kargs)
        end = time.process_time()
        print(end - start, "secondes se sont écoulées")

        return value

    return wrapper()

@time_it
def big_func():
    y = 0
    for x in range(1_000_000):
        y = x ** 2

    return y
