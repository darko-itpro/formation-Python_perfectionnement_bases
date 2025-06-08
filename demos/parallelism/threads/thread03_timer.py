"""
Démonstration des threads 03

Troisième exemple avec les threads, le début d'un des threads est retardé grâce à Timer.
"""

import demos.parallelism.logger_conf
import logging
import threading
import time

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish, duration):
    logging.info("Cooking %s started", dish)
    time.sleep(duration)
    logging.info("Cooking %s done", dish)

if __name__ == "__main__":
    logging.info("Main    : before creating thread")
    start_time = time.time()

    pasta_cook = threading.Thread(target=cooking, args=pasta)
    meat_cook = threading.Timer(pasta[1] - meat[1], cooking, args=meat)

    logging.info("Main    : cooking started")
    pasta_cook.start()
    meat_cook.start()

    pasta_cook.join()
    meat_cook.join()

    end_time = time.time()

    logging.info("Main    : Collecting after %.2f seconds, ready to serve", end_time - start_time)
