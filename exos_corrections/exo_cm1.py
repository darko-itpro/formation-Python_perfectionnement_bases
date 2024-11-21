import time

class TimeCounter:
    def __enter__(self):
        self.start = time.process_time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.process_time()

        print(end - self.start, "secondes se sont écoulées")

with TimeCounter():
    for x in range(1_000_000):
        y = x ** 2

