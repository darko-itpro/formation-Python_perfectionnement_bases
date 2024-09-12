
import demos.parallelism.logger_conf
import logging
#from threading import Thread as Task
from multiprocessing import Process as Task
import time

def countdown(n):
    while n > 0:
        n -= 1

def main():
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

    first_thread = Task(target=countdown, args=(value,))
    second_thread = Task(target=countdown, args=(value,))

    logging.info("Main    : before running thread")
    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    end_time = time.time()
    logging.info(f"Main    : Collecting after {end_time - start_time:.2f}")

if __name__ == '__main__':
    main()