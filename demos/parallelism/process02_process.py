"""
Démonstration des threads 02

Second exemple avec les threads, la durée est celle du programme principal
avant ajout des `.join()` où alors les actions se déroulent en parallèle.
"""

import demos.parallelism.logger_conf
import logging
import multiprocessing
import time

multiprocessing.Pipe()
multiprocessing.freeze_support()

pasta = ("pasta", 9)
meat = ("steak", 4)

def cooking(dish, duration):
    logging.info(f"Cooking {dish} started")
    time.sleep(duration)
    logging.info(f"Cooking {dish} done")

from multiprocessing import freeze_support
if __name__ == "__main__":
    freeze_support()
    logging.info("Main    : before creating thread")
    start_time = time.time()
    logging.info("Main    : wait for our cooking to finish")

    pasta_cook = multiprocessing.Process(target=cooking, args=pasta)
    meat_cook = multiprocessing.Process(target=cooking, args=meat)

    logging.info("Main    : before running thread")
    pasta_cook.start()
    meat_cook.start()

    end_time = time.time()
    logging.info(f"Main    : Collecting after {end_time - start_time:.2f} seconds, ready to serve")