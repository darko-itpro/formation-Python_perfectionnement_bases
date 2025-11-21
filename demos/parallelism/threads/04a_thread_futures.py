import demos.parallelism.logger_conf
import logging
import time

from concurrent.futures import ThreadPoolExecutor


pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish, duration):
    logging.info("Cooking %s started", dish)
    time.sleep(duration)
    logging.info("Cooking %s done", dish)

if __name__ == "__main__":
    logging.info("Main    : before creating thread")
    start_time = time.time()

    logging.info("Main    : cooking started")
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(cooking, *pasta)
        executor.submit(cooking, *meat)

    end_time = time.time()
    logging.info("Main    : Collecting after %.2f seconds, ready to serve", end_time - start_time)
