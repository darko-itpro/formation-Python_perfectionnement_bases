
import demos.parallelism.logger_conf
import logging
from threading import Thread
import time

def countdown(n):
    while n > 0:
        n -= 1

value = 100_000_000

logging.info("Main    : before sequential")
start_time = time.time()
countdown(value)
countdown(value)
end_time = time.time()
logging.info(f"Main    : Collecting after {end_time - start_time:.2f}")

print(" ----- ")

logging.info("Main    : before creating thread")
start_time = time.time()

first_thread = Thread(target=countdown, args=(value,))
second_thread = Thread(target=countdown, args=(value,))

logging.info("Main    : before running thread")
first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()

end_time = time.time()
logging.info(f"Main    : Collecting after {end_time - start_time:.2f}")
