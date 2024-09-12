import time

class Timer:
    def __enter__(self):
        self._start = time.process_time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.process_time()
        print(end - self._start, "secondes se sont écoulées")
        del self._start


with Timer():
    for x in range(1_000_000):
        y = x ** 2
