"""
Démonstration des threads 02

Second exemple avec les threads, la durée est celle du programme principal
avant ajout des `.join()` où alors les actions se déroulent en parallèle.
"""

import demos.parallelism.logger_conf
import logging
import threading
import time
import random

menu = [
    ("Burger with fries", 8),
    ("Hot Dog", 5),
    ("Pizza Napolitana", 4),
    ("Fish and chips", 7),
    ("Venison Stew", 10),
]

def cooking(dish, duration, call_event=None):
    logging.info(f"Cooking {dish} started")
    time.sleep(duration)
    logging.info(f"Cooking {dish} done")

    if call_event:
        call_event.set()

    logging.info(f"Cleaning for {dish}")
    time.sleep(2)
    logging.info(f"Cleaning for {dish} done")


if __name__ == "__main__":
    callback_event = threading.Event()

    logging.info("Main    : before creating thread")
    start_time = time.time()

    choice = random.choice(menu)
    cook = threading.Thread(target=cooking, args=(*choice, callback_event))

    logging.info("Main    : cooking started")
    cook.start()

    callback_event.wait()
    logging.info(f"Main    : Collecting after {time.time() - start_time:.2f} seconds, ready to serve")

    cook.join()
    logging.info(f"Main    : All done after {time.time() - start_time:.2f} seconds.")